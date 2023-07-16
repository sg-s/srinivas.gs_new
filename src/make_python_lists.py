"""module to make the html page for python lists"""

# TODO make this generic to all lists

import glob
import os

from jinja2 import Environment, FileSystemLoader

file_path = "/Users/srinivas/code/srinivas.gs/python.md"
with open(file_path, "r") as f:
    txt = f.readlines()


titles = []
links = []
text_blocks = []
ignore = True

paragraph = ""

for line in txt:
    if "##" not in line and ignore:
        continue

    ignore = False
    if "##" in line:
        if len(paragraph) > 0:
            text_blocks.append(paragraph)
            paragraph = ""

        title, link = line.split("]")
        titles.append(title.replace("## [", ""))
        link = link.replace(")\n", "")
        links.append(link[1:])

    else:
        paragraph += line

text_blocks.append(paragraph)


template_dir = "/Users/srinivas/code/srinivas.gs/templates"


environment = Environment(loader=FileSystemLoader(template_dir))
template_files = glob.glob(os.path.join(template_dir, "*.html"))
templates = dict()
for template in template_files:
    name = os.path.basename(template).replace(".html", "")
    templates[name] = environment.get_template(os.path.basename(template))


def make():
    cards = []
    for title, link, text in zip(titles, links, text_blocks):
        card = templates["card-no-img"].render(
            card_title=title, card_text=text, card_link=link
        )
        cards.append(card)

    html = templates["portfolio"].render(cards=cards)

    with open(
        "/Users/srinivas/code/srinivas.gs/lists/python/index.html", "w"
    ) as f:
        f.write(html)
