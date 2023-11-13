.PHONY: install virtualenv ipython lint test watch clean

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

formate:
	@.venv/bin/isort dundie tests integration
	@.venv/bin/black dundie tests integration

test:
	@.venv/bin/pytest -vv -s --cov=dundie --forked

watch:
	@.venv/bin/ptw -- -vv -s tests/ --cov=dundie --forked

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

docs:
	@mkdocs build --clean

docs-serve:
	@mkdocs serve

build:
	@python setup.py sdist bdist_wheel
