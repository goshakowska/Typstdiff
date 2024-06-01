# Project Configuration and Developer How-To

### Tools that were used in project development & their configuration, which might be useful to understand for any future contributors.
---
## Justfile

the easiest way for running unit tests, automated _Tox_ environments' tests, building package and documentation is by running `just` commands, which are defined in the Typstdiff package's Justfile:
```
# Justfile


install-deps:
    if [ -x "$(command -v poetry)" ]; then \
        poetry install; \
    else \
        pip install -r requirements.txt; \
    fi


test:
    if [ -x "$(command -v poetry)" ]; then \
        poetry run tox; \
    else \
        tox; \
    fi


format:
    if [ -x "$(command -v poetry)" ]; then \
        poetry run black src tests; \
    else \
        black src tests; \
    fi


docs:
    if [ -x "$(command -v poetry)" ]; then \
        cd documentation/ && poetry run mkdocs build; \
    else \
        cd documentation/ && mkdocs build; \
    fi


serve-docs:
    if [ -x "$(command -v poetry)" ]; then \
        cd documentation/ && poetry run mkdocs serve; \
    else \
        cd documentation/ && mkdocs serve; \
    fi


clean:
    rm -rf .tox .pytest_cache dist


build:
    if [ -x "$(command -v poetry)" ]; then \
        poetry build; \
    else \
        pip wheel . -w dist; \
    fi

```
Example command: `just install-deps`.


To be able to do that, the developer must meet the prerequisites, mentioned in the tool's repository README and download the package through provided commands (for the package manager of their choice): [Just Repository - installation](https://github.com/casey/just?tab=readme-ov-file#packages).


---
## Tox
Install tox using the pip package manager:
```
python -m pip install tox
```
Create a tox.ini configuration file inside the main project directory:
```
[tox]
requires =
    tox>=4
env_list = lint, type, py310, py311

[testenv]
description = run unit tests
deps =
    pytest>=7
    pytest-sugar
commands =
    pytest {posargs:tests}

[testenv:lint]
description = run linters
skip_install = true
deps =
    black==24.4.2
commands =
    black {posargs:.}
```
- [*tox*] - global settings
- [*testenv*] - settings for a specific test
- *envlist* - list of environments where tests will be run
- *skipsdist* - skip building distribution package
- *skip_install* - skip installation
- *deps* - required dependencies to run the test
- *commands* - commands to be executed as part of the test

In order to run all the tests for the Typstdiff package, format code using Black and test the package on different python interpreters / environments automatically, in terminal, within the main directory of the package, the `tox` command should be run.

Result, after running the aforementioned command:

```
  lint: OK (0.33=setup[0.04]+cmd[0.29] seconds)
  type: OK (25.02=setup[2.82]+cmd[22.20] seconds)
  py310: OK (22.50=setup[2.70]+cmd[19.80] seconds)
  py311: OK (23.68=setup[2.24]+cmd[21.44] seconds)
  congratulations :) (71.60 seconds)
```
---
## Testing
Package was tested via _pytest_ unit tests. Each of the .typst types, that are supported by the Typstdiff tool were tested in order to see if the changes (insertion, deletion, update) are marked appropriately in the output file. Aside from that complex files were tested - despite their higher complexity in structure the Typstdiff tool's performance did not worsened.
The tests are parameterized and they use pytest's @fixtures and @marks, in order to make the testing process more efficient.
---
## MkDocs
A tool used for creating project documentation.

### Installation and Configuration of MkDocs (Windows)

Install MkDocs using the pip package manager:

```
pip install mkdocs
``` 
Create a new project. The project name corresponds to the directory name where the documentation will be located.

```
mkdocs new <new project name>
```
Navigate to the MkDocs project directory.

```
cd .\<new project name>\
```
Run the MkDocs local server from the project directory.

```
mkdocs serve
```
Upon successful server start, the IP address will be displayed as the last log in the terminal. By default, it is [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

```
INFO    -  Building documentation...
INFO    -  Cleaning site directory`
INFO    -  Documentation built in 0.59 seconds
INFO    -  [HH:MM:SS] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [HH:MM:SS] Serving on http://127.0.0.1:8000/
```

---
## Poetry - tool for dependency management and packaging in Python

In order to install poetry You need to follow the steps below:

### Prerequisite

Install pipx: 

If You don't have `pipx` installed, follow the information in the [official pipx installation instructions](https://pipx.pypa.io/stable/installation/).

Pipx is used to install Python CLI applications globally while still isolating them in virtual environments. It will manage upgrades and uninstalls when used to install Poetry.

### Installation process

With pipx install Poetry:


```pipx install poetry```

This is the simplest way to install Poetry tool.

For more information follow the link to the official _poetry_ documentation and user guide:
[Poetry Introduction](https://python-poetry.org/docs/).

---
## Code Convention

Naming conventions follow PEP8 standard:

|  Type      |  Convention                                          |  Example                       |
| -----------|------------------------------------------------------|------------------------------- |
| Function   | Use lowercase letters and underscores for separation.| function, python_function     |
| Variable   | Use lowercase letters and underscores for separation.| x, var, python_variable       |
| Class      | Use uppercase letters, do not separate them.         | Model, PythonClass            |
| Method     | Use lowercase letters and underscores for separation.| class_method, method          |
| Constant   | Use uppercase letters, words separated by underscores.| CONSTANT, PYTHON_CONSTANT     |
| Module     | Use lowercase letters and underscores for separation.| module.py, python_module.py   |
| Package    | Use lowercase letters, do not separate them.         | package, pythonpackage        |

Names of variables, functions, classes, etc., should be descriptive.

```
>>> name = "John Smith"
>>> first_name, last_name = name.split()
>>> print(f"{last_name}, {first_name}")
'Smith, John'
```

Functions and classes at the top level should be separated by two blank lines on both sides.

```
class FirstClass:
    pass


class SecondClass:
    pass


def top_level_function():
    return None
```
Method definitions inside classes should be separated by a single blank line on both sides.


```
class ClassWithMethods:
    def first_method(self):
        return None

    def second_method(self):
        return None
```
Use blank lines inside functions to show distinct steps.


```
def calculate_variance(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers = sum_numbers + number
    mean = sum_numbers / len(numbers)

    sum_squares = 0
    for number in numbers:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(numbers)

    return mean_squares - mean**2
```
Limit the maximum line length to 79 characters.

```
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
```
```
from package import example1, \
    example2, example3
```
```
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```
If you need to break a line around binary operators such as + and *, you should do so before the operator.

```
total = (first_variable
         + second_variable
         - third_variable)
```
Closing parentheses should be placed either on the same line,

```
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```
or on a new line, consistently.
```
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```
Imports should be separated by a new line for each import.

```
# Correct:
import os
import sys
```
```
# Wrong:
import sys, os
```

Exception - the same library.
```
# Correct:
from subprocess import Popen, PIPE
```
Other good habits:

Recommended spacing around *parentheses*:

```
# Correct:
spam(ham[1], {eggs: 2})
foo = (0,)
if x == 4: print(x, y); x, y = y, x
```
Not recommended:
```
spam( ham[ 1 ], { eggs: 2 } )
bar = (0, )
if x == 4 : print(x , y) ; x , y = y , x
```
Recommended *separation of variables and operators*:
```
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
Not recommended:
```
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

Recommended *variable typing*:
```
def munge(input: AnyStr): ...
def munge() -> PosInt: ...
```
Not recommended:
```
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

Recommended *assigning values* to parameters within *function calls*:

```
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```
Not recommended:
```
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```
Recommended *assigning values* to parameters within *function definition*:
```
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```
Not recommended:
```
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```

