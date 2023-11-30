

.PHONY: build

install: 
	@echo "Installing srinivas.gs..."
	@bash install.sh

build: install
	poetry run python src/render_readmes.py


python:
	poetry run python src/make_python_lists.py
	open lists/python/index.html

youtube:
	poetry run python src/make_youtube_list.py
	open lists/youtube/index.html


jupyter:
	@echo "Installing kernel <site> in jupyter"
	-yes | jupyter kernelspec uninstall site
	poetry run python -m ipykernel install --user --name site
