

.PHONY: build

build:
	poetry run python src/make.py


jupyter:
	@echo "Installing kernel <site> in jupyter"
	-yes | jupyter kernelspec uninstall site
	poetry run python -m ipykernel install --user --name site
