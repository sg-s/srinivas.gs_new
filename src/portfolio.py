"""this module generates the portfolio page"""

import glob
import os
import pathlib

from jinja2 import Environment, FileSystemLoader

parent_dir = pathlib.Path(__file__).parent.parent.resolve()
template_dir = os.path.join(parent_dir, "templates")


environment = Environment(loader=FileSystemLoader(template_dir))
template_files = glob.glob(os.path.join(template_dir, "*.html"))
templates = dict()
for template in template_files:
    name = os.path.basename(template).replace(".html", "")
    templates[name] = environment.get_template(os.path.basename(template))


items = [
    (
        "Neural network dynamics visualization",
        "../assets/stg-embedding.png",
        "help text about this",
        ["bokeh", "data-visualization"],
        "https://srinivas.gs/stg/",
    ),
    (
        "IDEAS documentation",
        "../assets/ideas-docs.png",
        "help text about this",
        ["documentation", "mkdocs"],
        "https://inscopix.github.io/ideas-docs/calcium_imaging_qc.html",
    ),
    (
        "The xolotl neuron simulator",
        "../assets/X.png",
        "help text about this",
        ["neuroscience", "C++", "MATLAB", "ODEs"],
        "https://go.brandeis.edu/xolotl",
    ),
    (
        "pyvocab",
        "../assets/X.png",
        "A python-based vocabulary builder",
        ["streamlit", "python"],
        "https://go.brandeis.edu/xolotl",
    ),
    (
        "rent-or-buy",
        "img.link",
        "A streamlit app to help you decide whether to rent or buy a house",
        ["streamlit", "python"],
        "https://go.brandeis.edu/xolotl",
    ),
    (
        "IDEAS Quality Control Report",
        "../assets/ideas-qc.png",
        "help text about this",
        [
            "bokeh",
            "aws",
            "data-visualization",
            "calcium-imaging",
            "neuroscience",
        ],
        "https://inscopix.github.io/ideas-docs/qc_html/example-qc-report.html",
    ),
]


def make():
    cards = []

    for title, img_src, text, badges, link in items:
        card = templates["card"].render(
            badges=badges,
            card_title=title,
            card_text=text,
            img_src=img_src,
        )
        cards.append(card)

    html = templates["portfolio"].render(cards=cards)

    with open(
        "/Users/srinivas/code/srinivas.gs/portfolio/index.html", "w"
    ) as f:
        f.write(html)
