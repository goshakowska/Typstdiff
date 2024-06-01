# Justfile

# Task to install dependencies using Poetry or pip
install-deps:
    if [ -x "$(command -v poetry)" ]; then \
        poetry install; \
    else \
        pip install -r requirements.txt; \
    fi

# Task to run tests using tox or directly with pytest
test:
    if [ -x "$(command -v poetry)" ]; then \
        poetry run tox; \
    else \
        tox; \
    fi

# Task to format all of the code in the package using black
format:
    if [ -x "$(command -v poetry)" ]; then \
        poetry run black src tests; \
    else \
        black src tests; \
    fi

# Task to build the documentation using MkDocs
docs:
    if [ -x "$(command -v poetry)" ]; then \
        cd documentation/ && poetry run mkdocs build; \
    else \
        cd documentation/ && mkdocs build; \
    fi

# Task to serve the documentation locally
serve-docs:
    if [ -x "$(command -v poetry)" ]; then \
        cd documentation/ && poetry run mkdocs serve; \
    else \
        cd documentation/ && mkdocs serve; \
    fi

# Task to clean the project (remove .tox, .pytest_cache, etc.)
clean:
    rm -rf .tox .pytest_cache dist

# Task to build the package using Poetry or pip
build:
    if [ -x "$(command -v poetry)" ]; then \
        poetry build; \
    else \
        pip wheel . -w dist; \
    fi
