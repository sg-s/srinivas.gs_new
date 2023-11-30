"""module to make the html page for python lists"""

# TODO make this generic to all lists

import glob
import os

import marko
from jinja2 import Environment, FileSystemLoader
from pywebcopy import save_webpage
from urllib3.util import parse_url

file_path = "/Users/srinivas/code/srinivas.gs/lists/python.md"
with open(file_path, "r") as f:
    txt = f.readlines()


titles = []
links = []
text_blocks = []
ignore = True
hostnames = []

paragraph = ""

for line in txt:
    if "##" not in line and ignore:
        continue

    ignore = False
    if "##" in line:
        if len(paragraph) > 0:
            text_blocks.append(marko.convert(paragraph))
            paragraph = ""

        title, link = line.split("]")
        titles.append(title.replace("## [", ""))
        link = link.replace(")\n", "")
        links.append(link[1:])

        hostname = parse_url(link[1:]).hostname
        hostnames.append(hostname)

    else:
        paragraph += line

text_blocks.append(marko.convert(paragraph))


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

    cards = []
    for title, link, text, hostname in zip(
        titles,
        links,
        text_blocks,
        hostnames,
    ):
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

        card = templates["card-no-img"].render(
            card_title=title,
            card_text=text,
            card_link=link,
            card_subtitle=hostname,
            header=header,
            card_style=card_style,
        )
        cards.append(card)

    html = templates["portfolio"].render(
        cards=cards,
        title="Python Reading List",
        lead_paragraph="A list of useful python-related things I've seen.",
    )

    with open(
        "/Users/srinivas/code/srinivas.gs/lists/python/index.html", "w"
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
