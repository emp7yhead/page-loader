.DEFAULT_GOAL = help

install:  ## Install dependencies with poetry
	poetry install

page-loader:  ## Run Page Loader
	poetry run page-loader

build:  ## Build package
	poetry build

package-install:  ## Install package
	pip install --user dist/*.whl

lint:  ## Check lint
	poetry run flake8 page_loader

test:  ## Check tests
	poetry run pytest

type:  ## Type check
	poetry run mypy page_loader

check: lint test type  ## Complete check (linter, tests, typechecking)

test-coverage:  ## Create test coverage
	poetry run pytest --cov=page_loader --cov-report xml

help:  ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | sort \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[0;32m%-30s\033[0m %s\n", $$1, $$2}'
