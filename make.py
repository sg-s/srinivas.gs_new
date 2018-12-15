#! /usr/bin/env python
# makes HTML pages from markdown source, iteratively, in each folder

import codecs, os, markdown


all_paths = []

for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith("README.md"):
             all_paths.append(os.path.join(root, file))

for path in all_paths:

	print(path)

	path_root = path.replace('README.md','')

	# make the html from README.md
	input_file = codecs.open(path, mode="r", encoding="utf-8")
	text = input_file.read()
	html = markdown.markdown(text, extensions=['markdown.extensions.extra'])

	html = html.replace('<table>','<table id="example" class="display" cellspacing="0" width="80%">')

	output_file = codecs.open(path.replace('README.md','body.html'), "w", encoding="utf-8")
	output_file.write(html)
	output_file.close()


	# cat the header and body and footer
	filenames = ['header.html', 'body.html', 'footer.html']
	filenames = [path_root + filename for filename in filenames]

	with open(path_root+'index.html', 'w') as outfile:
	    for fname in filenames:
	        with open(fname) as infile:
	        	# print(infile.read())
	            outfile.write(infile.read())

	os.remove(path_root+'body.html')
