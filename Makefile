install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

build:
	poetry build

.PHONY: install test lint build
