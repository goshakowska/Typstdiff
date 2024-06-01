# Justfile


# Task to install dependencies using Poetry
install-deps:
    poetry install

# Task to run tests using tox
test:
    poetry run tox

# Task to format all of the code in the package
format:
    poetry run black

# Task to format the tests using black linter
format_code:
    poetry run black src tests

# Task to format the source code using black linter
format_tests:
    poetry run black tests

# Task to build the documentation using MkDocs
docs:
    cd documentation/ && poetry run mkdocs build

# Task to serve the documentation locally
serve-docs:
    cd documentation/ && poetry run mkdocs serve

# Task to clean the project (remove .tox, .pytest_cache, etc.)
clean:
    rm -rf .tox .pytest_cache dist

# Task to build the package using Poetry
build:
    poetry build
