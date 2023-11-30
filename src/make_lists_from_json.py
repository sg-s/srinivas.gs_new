"""this module makes HTML pages from JSON files
that specify lists"""

from src import utils

files = utils.find_all_json_files()
for file in files:
    print(str(file), end=" ")
    utils.json_to_html(str(file))
    print("✅")
