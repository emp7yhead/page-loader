install:
		poetry install

page-loader:
		poetry run page-loader

build:
		poetry build

package-install:
		pip install --user dist/*.whl

make lint:
		poetry run flake8 page-loader

test-coverage:
	poetry run pytest --cov=page-loader --cov-report xml