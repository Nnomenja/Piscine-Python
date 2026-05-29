VENV = .venv

all:
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate && \
	pip install --upgrade pip && \
	pip install flake8 mypy

fclean:
	rm -rf $(VENV)
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

active:
	. $(VENV)/bin/activate

lint: flake mypi

flake:
	@find . -type f -name "ft_*.py" \
	-not -path "./venv/*" \
	-exec $(VENV)/bin/flake8 {} +

mypi:
	@find . -type f -name "ft_*.py" \
	-not -path "./venv/*" \
	-exec $(VENV)/bin/mypy {} + \

.PHONY: all fclean active