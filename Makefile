

.PHONY: build

build:
	poetry run python src/make.py


python:
	poetry run python src/make_python_lists.py
	open lists/python/index.html

jupyter:
	@echo "Installing kernel <site> in jupyter"
	-yes | jupyter kernelspec uninstall site
	poetry run python -m ipykernel install --user --name site
