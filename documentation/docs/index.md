# TypstDiff documentation


For the source code visit [Gitlab](https://gitlab-stud.elka.pw.edu.pl/dferfeck/zprp-typstdiff).


## Documentation commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout
    assets/                             # Folder for examples files used to comparing with typstdiff
        example1/                       # Files for example1 (check pdf for example)
        example2/                       # Files for example2 (check pdf for example)
    dist/                               # Folder for tar of package typstdiff
    documentation/
        mkdocs.yml                      # The configuration file
        docs/
            index.md                    # The documentation homepage
            about.md                    # About project
            bibliography.md             # Sources used in the project
            project_configuration.md    # Main information about project configuration
            user_how_to.md              # User guide
    tests/
            test_complex/               # Files used for tests in test_complex.py
            test_working_types/         # Files used for tests in test_typstdiff.py
            test_complex.py             # Complex tests for groups and more nested typst
            test_typstdiff.py           # Units tests for each of working type
    typstdiff/                          # Main folder with tool's source files
            __init__.py
            comparison.py               # Main Comparison class which compares typst documents and marks changes
            errors.py                   # Custom typstdiff exceptions 
            file_converter.py           # FileConverter class to convert files between typst and json, and compile typst documents to pdf
            main.py                     # Runs typstdiff, handles user arguments from console
    .gitignore
    design_propasal_z04.pdf
    pyproject.toml
    README.md
    tox.ini

