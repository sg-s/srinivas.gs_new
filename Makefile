

repo=$(shell basename $(CURDIR))

.PHONY: build

install: 
	@echo "Installing srinivas.gs..."
	@bash install.sh

build: install
	poetry run python src/render_readmes.py
	poetry run python src/make_lists_from_json.py


python:
	poetry run python src/make_python_lists.py
	open lists/python/index.html

youtube:
	poetry run python src/make_youtube_list.py
	open lists/youtube/index.html


jupyter:
	@echo "Installing kernel  $(repo) in jupyter"
	-yes | jupyter kernelspec uninstall $(repo)
	poetry run python -m ipykernel install --user --name $(repo)