install: 
	poetry install

build: 
	poetry build

package-install: 
	pip3 install --user dist/*.whl

selfcheck:
	poetry check

make lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv --cov=gendiff --cov-report xml tests
