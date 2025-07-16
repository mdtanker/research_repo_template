# Research repo template

This template is a a useful starting point if you have code you need to share with others, such as fulfulling an open-access requirement for submission to a journal. Once the instructions below are completed, users can clone your GitHub repository, install the code locally, run your tests and analysis.

Here are a few features offered in this template:
* styling tools to help clean up your code and highlight issues in it that you should fix
* instructions for defining your code's dependencies
* tools for creating and maintaining a conda environment.
* instructions for testing your code with pytest.
* optional automatic syncing of your repository to Zenodo for archiving and assigning a DOI.

This template is a based on the [Scientific Python Development Guide](https://learn.scientific-python.org/development/). The main differences with the [template they provide](https://github.com/scientific-python/cookie) is that this is an _opinionated_ and _simplified_ template, where I made certain decision I feel are optimal. Additional, this is intended for sharing code, which users can clone and install locally, but is not intended for packaging your code into a packaged installable with `pip` or `conda`. I have a [separate template intended for packaging.](https://github.com/mdtanker/python_package_template)

## Template Instructions

Steps:
1) Initiate your repository:
    - On this [template's page](https://github.com/mdtanker/research_repo_template), click the `Use this template` button to `Create a new repository`.
    - choose a project name
        - for simplicity, this name will be used for all of the follow: the folder name that holds this repository as well as the code folder under `src/`, and the repository name on GitHub. The best choice is a lowercase word with no spaces or punctuation, but if necessary capitalization and underscores can be included.
    - choose if you want the repository in your personal account or in one of your organization's accounts.
    - add a 1 sentence description of the project.
    - choose public or private. This can be changed later, but to be published on Zenodo, it needs to be public.
    - create the repository
2) Update this template:
    - clone your repository to your computer with `git clone <url of the github repo>`.
    - change all instances of `projectname` in this repository with your chosen name. (If use a program like VSCode use a `search and replace` function (i.e. `ctrl+f`)).
        - this includes the folder name of `src/projectname/`
    - add your name to Line 9 of `pyproject.toml`
    - replace `organizationname/projectname` with your GitHub organization (or personal) account name and projectname on lines 50-52 of `pyproject.toml`
    - update `pyproject.yml` with a description (1 sentence) and keywords ()
    - add a description of your project at the bottom of this README.
    - at this point, it might be good to make your initial commit to your repository with the following git commands:
        ```bash
        git checkout -b new-branch
        git add .
        git commit -m "initialize template with names"
        git push -u origin new-branch
        ```
    - in the GitHub repository, go to the `Pull request` tab and open a PR for your changes. Merge this into main.
3) Pull in your merged changes
    - how you do this depends if you pushed your changed directly to the repository, or through a fork of the repository:
        1) PR submitted directly to repository:
            - fetch your recent changes: `git fetch`
            - checkout your main branch: `git checkout main`
            - OPTIONAL: delete your feature branch: `git branch -d new-branch`
            - pull in your changes: `git pull`
        2) PR submitted through a fork:
            - fetch your recent changes: `git fetch upstream`
            - checkout your main branch: `git checkout main`
            - OPTIONAL: delete your feature branch: `git branch -d new-branch`
            - merge changes from upstream: `git merge upstream/main`
                - this syncs your local repository to the upstream one
            - push your changes to your upstream (forked) repository: `git push origin main`
4) Add your code
    - decide on a module name(s)
        - these need to be lowercase, should be short and while possible, shouldn't include underscores.
        - if your project is going to be small, a single module with the same name as the project is fine. If it's going to be more than a few hundred lines of code, it's best to separate your code into distinct modules which perform similar tasks. - for each module you want do the following:
            - create / rename the existing file: `src/projectname/module1.py`
            - create / rename the test file: `tests/test_module1.py`
            - replace all instances of `module1` with your module's name.
    - add your code to your module `.py` files.
    - you have two options for how users can import your code.
        1) ```python
            from projectname import module1

            module1.function1()
            ```
            - this option is available by default for any functions you write, and is nice if you have several modules because it clearly shows where the code is coming from.
        2) ```python
            import projectname

            projectname.function1()
            ```
            - to allow `function1` to be imported as above, you need to manually add it to the list in `src/projectname/_init_.py`. If you only have 1 module, this may be a better technique.
    - add tests for your modules' test file in `tests/`.
5) Specify your dependencies
    - dependencies for your code should typically only be those that are directly used (imported) in your source code (or are explicitly needed but not import), but not the dependencies of your dependencies.
    - core dependencies are specified in `pyproject.toml` under the `[project]` section with the format `dependencies = ["pandas", "scipy>=1.0"]`.
    - optional dependencies are specified in `pyproject.toml` under the `[dependency-groups]` section with the following format, for example for optional visualization dependencies: `viz = ["matplotlib",]`.
    - Dependency version's should only be constrained to specific versions if you know there is an issue, and they should almost never be pinned to specific versions, as this will cause many issues for anyone who wants to use your package in their own environments.
    - this template also includes files and commands to create `conda` environments. You need to manually ensure the dependencies listed in `environmental.yml` match those in `pyproject.toml`. Include all optional dependencies in the `environmental.yml`. If a dependency is only available via pip, and not conda, add it at the bottom to be installed via pip.
6) Setting up your environment
    - create a new conda environment based on the dependencies in your `environment.yml` file, and install your code in editable mode into it. Editable means if you change the code, the environment will include those changes without have to re-install the code. However, you will need to restart your Jupyter kernel if using notebooks to get the updated code.
    - Note that `mamba` can be replaced by `conda`.
    ```bash
    mamba env create --file environment.yml
    mamba activate projectname
    pip install --no-deps -e .
    ```
    - for convienance, if you have the tool `Make` installed, you can use the equivalent commands:
    ```bash
    make create
    mamba activate projectname
    make install
    ```
7) Run `pre-commit` code checks
    - `pre-commit` offers some tools for auto-formatting your code, and checking for common issues and bugs. The specific tools that are run are defined in `.pre-commit.config.yaml`. To run pre-commit, we use another tool called `nox`, install it with `pip install nox`.
    - run pre-commit with `nox -s lint`.
    - run it again to remove warnings about the things that were auto-fixed
    - this will likely give you lots of warnings about miss-spellings, and issues like your code not have docstrings or missing / incorrect type annotations. Either fix these warnings in your code, or if you really don't care about things like docstrings or type annotations, you can disable some checks in `.pre-commit.config.yaml`.
    - if you want to ignore a warning on a specific line, you can add this to the end of the line:  `# noqa: code` where code is the warning you want to suppress.
8) Enable `pre-commit` to run automatically
    - install and enable it with `pre-commit install`
9) Run `pylint` linting checks.
    - `pylint` is a very opinionated tool for checking python code for common issues and adhering to best-practises. `pylint` is configured in `pyprojec.toml`, and we run it with `nox`: `nox -s pylint`.
    - this will likely give you lots of warnings. Go through these and try and fix them all. If you want to ignore a specific warning on a specific line, add this to the end: `# pylint: disable=warning-message` where warning-message is the warning you want to suppress.
10) Set up automated Zenodo releases
    - if you haven't already, link your organization (or personal) GitHub account to [Zenodo](https://zenodo.org/) using `Linked accounts` under your Zenodo profile.
    - do to the `GitHub` menu on your Zenodo profile.
    - click the Sync button and then turn on the switch for your repository.
    - any future GitHub releases ('make a release' button) should now result in a new Zenodo release and DOI automatically.
11) Finalize
    - remove all the above instructions and raise any issues in this template's repository if you have any suggestion or found any errors in this template!

# projectname
Short description of your code.


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

   nox -s style

Test your code

    nox -s test

To update dependencies, first add or change dependencies listed in `environment.yml`, then with your conda environment activated run:

    make update

When writing code; use logging to inform users of info, errors, and warnings. In each module `.py` file, import the project-wide logger instance with `from projectname import logger` and then for example: `logger.info("log this message")`
