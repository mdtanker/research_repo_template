# Research repo template

This template is a a useful starting point if you have code you need to share with others, such as fulfulling an open-access requirement for submission to a journal. Once the instructions below are completed, users can clone your GitHub repository, install the code locally, run your analysis.

Here are a few features offered in this template:
* styling tools to help clean up your code and highlight issues in it that you should fix
* instructions for defining your code's dependencies
* tools for creating and maintaining a conda environment.
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
2) Update this template:
    - clone your repository to your computer with `git clone <url of the github repo>`; if you create the repository on an organization's GitHub instead of your personal one, first fork the repository before you clone it.
    - change all instances of `projectname` in this repository with your chosen name. (If use a program like VSCode use a `search and replace` function (i.e. `ctrl+f`)), there should be ~30 instances of `projectname`.
        - this includes the folder name of `src/projectname/`
    - add your name to Line 8 of `pyproject.toml`
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
        - if your project is going to be small, a single module with the same name as the project is fine. If it's going to be more than a few hundred lines of code, it's best to separate your code into distinct modules which perform similar tasks.
        - for each module you want do the following:
            - create / rename the existing file: `src/projectname/module1.py`
            - replace all instances of `module1` with your module's name.
    - add your code to your module `.py` files.
    - in your notebooks or python scripts you should import your local code with `import projectname`.
    - To access a function / class you via `projectname.functionname`, you have to add the function or class names to the file `src/projectname/_init_.py`.
5) Specify your environment and  dependencies
    - dependencies for your code should typically only be those that are directly used (imported) in your source code (or are explicitly needed but not import), but not the dependencies of your dependencies.
    - add these dependencies to the `environment.yml` file. Users can recreate an environment from this file with `conda env create --file environment.yml`
    - if you know your package has an issue with a specific version of a dependency, you can set a max or min version with `scipy>=1.0`
    - if a dependency is only available via pip, and not conda, add it at the bottom to be installed via pip.

### Optional steps
6) Setup code-style checks
    - install nox with `pip install nox`
    - run style checks with `nox -s style`
    - install pre-commit with `pip install pre-commit`
    - set pre-commit to run for all local commits with `pre-commit install`
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
