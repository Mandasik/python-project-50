install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

lint:
	poetry run flake8 gendiff

p_test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov
