# Research repo template
Template for creating repositories for research projects using Python

Steps:
1) choose a project name (no spaces, capitals or underscores) and replace `projectname` with it in the following locations:
    - `Makefile` top line
    - `environment.yml` top line
    - `src/projectname` folder
    - `projectname.py` in `src/projectname/`
    - line 6 of `pyproject.toml`
    - `project.urls` section of `pyproject.toml`
    - import line of `tests/test_module1.py`
2) add your pip/conda dependencies to `environmental.yml`
3) update `pyproject.yml`
    - update your name and email
    - add a description
    - add keywords
    - replace `mdtanker` with your github username in the `project.urls` section
4) add your code to and rename `src/projectname/module1.py`
5) add any functions you want available on import to the list in `src/projectname/_init_.py`
6) add tests for `module1.py` to `tests/test_module1.py` and rename to your module
7) remove all the above instructions and add a description of your project here, and tweak the below user instructions as needed


## Getting the code

You can download a copy of all the files for this project by cloning the GitHub repository:

    git clone https://github.com/mdtanker/projectname

## Dependencies

These instructions assume you have `Make` installed. If you don't you can just open up the `Makefile` file and copy and paste the commands into your terminal. This also assumes you have Python installed.

Install the required dependencies with either `conda` or `mamba`:

    cd projectname

    make create

Activate the newly created environment:

    mamba activate projectname

Install the local project

    make install


## How to use

To use this code, you need to first import the package. There are two options:

### 1: Import the main function

For example:
```python
import projectname
```

will allow you to access the function `example_function()` with either `projectname.module1.example_function()` or just `projectname.example_function()`.

Functions accessed in this way need to be explicitly added to the file `src/projectname/__init__.py`

### 2: Import each module individually

For example:
```python
from projectname import module1
```
Will allow you to access the function `example_function()` with `module1.example_function()`.


## Developer instructions

Style-check your code:

    make style

Test your code

    make test

To update dependencies, first add or change dependencies listed in `environment.yml`, then with your conda environment activated run:

    make update

When writing code; use logging to inform users of info, errors, and warnings. In each module `.py` file, import the project-wide logger instance with `from projectname import logger` and then for example: `logger.info("log this message")`
