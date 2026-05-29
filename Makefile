VENV = venv

all:
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate && \
	pip install --upgrade pip && \
	pip install flake8 mypy

fclean:
	rm -rf $(VENV)

.PHONY: all fclean