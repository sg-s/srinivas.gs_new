"""this module defines some core functions we can call"""


from src.utils import find_all_json_files, json_to_html


def make():
    """make the entire website

    this wrapper calls all other functions
    """

    print("🚧 Making HTML files from JSON sources...")

    files = find_all_json_files()
    for file in files:
        print(f"  🗂️  {file}")
        json_to_html(str(file))
