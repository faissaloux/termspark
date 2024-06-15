NAME = termspark
PYTHON = python3

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf *_cache
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .coverage
	find $(NAME) tests -type d -name '__pycache__' -exec rm -rf {} +

install: clean
	pip install -e ."[dev]"

install_docs: clean
	pip install -e ."[docs]"

update_docs_changelog: clean
	cp CHANGELOG.md docs/changelog.md

build_docs: clean
	mkdocs build -d docs_build

deploy_docs: clean
	mike deploy --push 2.x

build: clean
	$(PYTHON) setup.py bdist_wheel

test: clean
	pytest --cov -v

lint: mypy

format:
	isort .
	black .

mypy:
	mypy --show-error-codes $(NAME) tests

black:
	black . --check

isort:
	isort . --check-only

precommit: clean
	pre-commit run --all-files
