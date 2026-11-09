.PHONY: test lint
test:
	python -m pytest -q
lint:
	ruff check src tests experiments scripts
