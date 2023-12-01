"""core utilities to make site"""


import json
import os
from pathlib import Path

import jinja2
import marko
from beartype import beartype
from jinja2 import Template

repo_root = Path(__file__).parent.parent


@beartype
def _get_template(name: str) -> jinja2.environment.Template:
    """helper function to get a tempalte from a file"""
    template_dir = os.path.join(repo_root, "templates")

    template_file = os.path.join(template_dir, name + ".html")

    with open(template_file) as file:
        template = Template(file.read())

    return template


@beartype
def json_to_html(json_file_loc: str) -> None:
    """this function converts a JSON file into a HTML file

    the JSON file is exepected to have a list of items,
    and to specify a template to use.
    """
    with open(json_file_loc, "r") as file:
        data = json.load(file)

    # convert links from md
    for key in data.keys():
        if "](" in data[key]:
            data[key] = marko.convert(data[key])

    items = []
    for item in data["items"]:
        item["text"] = marko.convert(item["text"])

        template = _get_template(data["template"])

        card = template.render(
            **item,
        )
        items.append(card)

    data["items"] = items

    template = _get_template("masonry")

    html = template.render(**data)

    html_file_loc = json_file_loc.replace(".json", ".html")
    with open(html_file_loc, "w") as f:
        f.write(html)


def find_all_json_files():
    """finds all index.json files in the repo"""
    return Path(repo_root).rglob("*index.json")
