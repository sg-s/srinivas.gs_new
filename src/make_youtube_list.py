"""module to make the html page for python lists"""

# TODO make this generic to all lists

import glob
import os

from jinja2 import Environment, FileSystemLoader
from pywebcopy import save_webpage
from urllib3.util import parse_url

file_path = "/Users/srinivas/code/srinivas.gs/lists/youtube.md"


# parse a md file


template_dir = "/Users/srinivas/code/srinivas.gs/templates"


environment = Environment(loader=FileSystemLoader(template_dir))
template_files = glob.glob(os.path.join(template_dir, "*.html"))
templates = dict()
for template in template_files:
    name = os.path.basename(template).replace(".html", "")
    templates[name] = environment.get_template(os.path.basename(template))


tokens = ("@important", "@talk")


def make():
    """makes the HTML page from the markdown page"""

    # check every link to make sure it's online

    all_items = parse_md_file(file_path)

    cards = []
    for item in all_items:
        text = item["text"]

        if "@talk" in text:
            header = "talk"
        else:
            header = False

        if "@important" in text:
            card_style = "text-bg-primary"
        else:
            card_style = ""

        for token in tokens:
            text = text.replace(token, "")

        card = templates["youtube-card"].render(
            card_title=item["title"],
            card_text=text,
            card_link=item["link"],
            links=item["list_items"],
            header=header,
            card_style=card_style,
            img_src=item["title"].lower().strip() + ".jpg",
        )
        cards.append(card)

    html = templates["portfolio"].render(
        cards=cards,
        title="YouTube channels I watch",
        lead_paragraph="A list of useful python-related things I've seen.",
    )

    with open(
        "/Users/srinivas/code/srinivas.gs/lists/youtube/index.html", "w"
    ) as f:
        f.write(html)


# TODO fix this
# save_webpage(
#     url="https://gto76.github.io/python-cheatsheet/",
#     project_folder="/Users/srinivas/code/srinivas.gs/",
#     project_name="caches",
#     debug=False,
#     open_in_browser=False,
# )


if __name__ == "__main__":
    make()
