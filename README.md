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
    - on this [template's page](https://github.com/mdtanker/research_repo_template), click the `Use this template` button to `Create a new repository`.
    - choose a project name
        - for simplicity, this name will be used for all of the follow: the folder name that holds this repository as well as the code folder under `src/`, and the repository name on GitHub. The best choice is a lowercase word with no spaces or punctuation, but if necessary capitalization and underscores can be included.
    - choose if you want the repository in your personal account or in one of your organization's accounts.
    - add a 1 sentence description of the project.
    - choose public or private. This can be changed later, but to be published on Zenodo, it needs to be public.
    - create the repository
    - update any repository settings, below are my recommended settings:
        - enable discussions
        - only allow squash merging (disable the other options)
        - always suggest updating pull request branches
        - automatically delete head branches
        - protect the main branch so any changes to it need to be made through a Pull Request.
            - go to the repository's `Settings`, `Branches`, `Add branch ruleset`. Name it "protected_main", make the `Enforecement status` Active, include the Default branch as the target, and check the following `Rules`: `Restrict deletion`, `Require a pull request before merging`, only allow `Squash` as a merge method, and `Block force pushes`.
2) Update this template:
    - clone your repository to your computer with `git clone <url of the github repo>`; if you create the repository on an organization's GitHub instead of your personal one, first fork the repository before you clone it.
    - change all instances of `projectname` in this repository with your chosen name. (If use a program like VSCode use a `search and replace` function (i.e. `ctrl+f`)), there should be ~50 instances of `projectname`.
        - this includes the folder name of `src/projectname/`
    - add your name to Line 9 of `pyproject.toml`
    - replace all instances of `organizationname` with your GitHu organization (or personal) account name, whichever is going to host the repository.
    - update `pyproject.yml` with a description (1 sentence) and keywords.
    - add a description of your project here in the README.
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
    - if you know your package has an issue with a specific version of a dependency, you can set a max or min version with "scipy>=1.0".
    - dependencies should almost never be pinned to specific versions, as this will cause many issues for anyone who wants to use your package in their own environments.
    - for standard scientific packages (i.e., `pandas`, `xarray`, and `numpy`), as well as the version of Python, it's recommended to set minimum support versions following the timeline of [SPEC 0 guidelines](https://scientific-python.org/specs/spec-0000/).
    - this template also includes files and commands to create `conda` environments. You need to manually ensure the dependencies listed in `environment.yml` match those in `pyproject.toml`. Include all optional dependencies in the `environment.yml`. If a dependency is only available via pip, and not conda, add it at the bottom to be installed via pip.
6) Create environment, style check, test, and commit your changes.
    - follow the instructions in `CONTRIBUTING.md` starting at section `Setting up nox`.
    - these steps should result in a merged PR with your code.
7) Set up automated Zenodo releases
    - if you haven't already, link your organization (or personal) GitHub account to [Zenodo](https://zenodo.org/) using `Linked accounts` under your Zenodo profile.
    - do to the `GitHub` menu on your Zenodo profile.
    - click the Sync button and then turn on the switch for your repository.
    - any future GitHub releases should now result in a new Zenodo release and DOI automatically.
8) Finalize
    - remove all the above instructions and raise any issues in this template's repository if you have any suggestion or found any errors in this template!

# projectname
Short description of your code.


## Getting the code

You can download a copy of all the files for this project by cloning the GitHub repository:

    git clone https://github.com/organizationname/projectname

## Dependencies

These instructions assume you have Python (>=3.11) installed. If you don't we recommend installing it with [miniforge](https://github.com/conda-forge/miniforge) for a simple and minimal setup.

Install the required dependencies with either `conda` or `mamba`:

    cd projectname

    mamba env create --file environment.yml --name projectname

Activate the newly created environment:

    mamba activate projectname

Install the local project

    pip install --no-deps -e .


# How to contribute / develop?

See the file `CONTRIBUTING.md` for some detailed instructions on how to work on developing this repository.
