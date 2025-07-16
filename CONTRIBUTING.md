# How to contribute

## TLDR (Too long; didn't read)
* OPTIONAL: if you're contributing to someone else's repository, first [fork](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) the main [repository](https://github.com/organizationname/projectname) using the `Fork` button on GitHub.
* clone the (forked) repository on your computer: `git clone https://github.com/organizationname/projectname`.
* [create a branch](https://docs.github.com/en/get-started/using-github/github-flow#create-a-branch) for your edits: `git checkout -b new-branch`
* make your changes
* run the style checkers: `nox -s style`
* add your changed files: `git add .`
* once the style checks pass, commit your changes: `git commit -m "a short description of your changes"`
* push your changes: `git push -u origin new-branch`
* [make a Pull Request](http://makeapullrequest.com/) for your branch from the main GitHub repository [PR page](https://github.com/organizationname/projectname/pulls).

🎉 Thanks for considering contributing to this package! 🎉

<sub>Adapted from the great contribution guidelines of the [Fatiando a Terra](https://www.fatiando.org/) packages<sub>.

> This document contains some general guidelines to help with contributing to this code. Contributing to a package can be a daunting task, if you want help please reach out on the [GitHub discussions page](https://github.com/organizationname/projectname/discussions)!

Any kind of help would be much appreciated. Here are a few ways to contribute:
* 🐛 Submitting bug reports and feature requests
* 📝 Writing tutorials or examples
* 🔍 Fixing typos and improving to the documentation
* 💡 Writing code for everyone to use

If you get stuck at any point you can create an issue on GitHub (look for the Issues tab in the repository).

For more information on contributing to open source projects,
[GitHub's own guide](https://guides.github.com/activities/contributing-to-open-source/)
is a great starting point if you are new to version control.
Also, checkout the
[Zen of Scientific Software Maintenance](https://jrleeman.github.io/ScientificSoftwareMaintenance/)
for some guiding principles on how to create high quality scientific software
contributions.


## Contents

* [What Can I Do?](#what-can-i-do)
* [Reporting a Bug](#reporting-a-bug)
* [Editing the Documentation](#editing-the-documentation)
* [Contributing Code](#contributing-code)
  - [General guidelines](#general-guidelines)
  - [Fork the repository](#fork-the-repository)
  - [Clone the repository](#clone-the-repository)
  - [Setting up Nox](#setting-up-nox)
  - [Setting up your environment](#setting-up-your-environment)
  - [Make a branch](#make-a-branch)
  - [Make your changes](#make-your-changes)
  - [Testing your code](#testing-your-code)
  - [Documentation](#documentation)
  - [Committing changes](#committing-changes)
  - [Push your changes](#push-your-changes)
  - [Open a PR](#open-a-pr)
  - [Code review](#code-review)
* [Publish a new release](#publish-a-new-release)
* [Update the Dependencies](#update-the-dependencies)

## What Can I Do?

* Tackle any issue that you wish! Some issues are labeled as **"good first issues"** to
  indicate that they are beginner friendly, meaning that they don't require extensive
  knowledge of the project.
* Make a tutorial or example of how to do something.
* Provide feedback about how we can improve the project or about your particular use
  case.
* Contribute code you already have. It doesn't need to be perfect! We will help you
  clean things up, test it, etc.

## Reporting a Bug

Find the *Issues* tab on the top of the GitHub repository and click *New Issue*.
You'll be prompted to choose between different types of issue, like bug reports and
feature requests.
Choose the one that best matches your need.
The Issue will be populated with one of our templates.
**Please try to fillout the template with as much detail as you can**.
Remember: the more information we have, the easier it will be for us to solve your
problem.

## Editing the Documentation

If you're browsing the documentation and notice a typo or something that could be
improved, please consider letting us know by [creating an issue](#reporting-a-bug) or
submitting a fix (even better 🌟). You can submit fixes to the documentation pages completely online without having to
download and install anything:

* On each documentation page, there should be a "✏️" bottom at the very top.
* Click on that link to open the respective source file on GitHub for editing online (you'll need a GitHub account).
* Make your desired changes.
* When you're done, scroll to the bottom of the page.
* Fill out the two fields under "Commit changes": the first is a short title describing your fixes, the second is a more detailed description of the changes. Try to be as detailed as possible and describe *why* you changed something.
* Click on the "Commit changes" button to open a pull request (see below).
* We'll review your changes and then merge them in if everything is OK.
* Done 🎉🍺

Alternatively, you can make the changes offline to the files in the `doc` folder or the
example scripts. See [Contributing Code](#contributing-code) for instructions.

## Contributing Code

**Is this your first contribution?**
Please take a look at these resources to learn about git and pull requests (don't
hesitate to ask questions in the [GitHub discussions page](https://github.com/organizationname/projectname/discussions)):

* [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).
* Aaron Meurer's [tutorial on the git workflow](http://www.asmeurer.com/git-workflow/)
* [How to Contribute to an Open Source Project on GitHub](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github)

If you're new to working with git, GitHub, and the Unix Shell, we recommend
starting with the [Software Carpentry](https://software-carpentry.org/) lessons,
which are available in English and Spanish:

* [Version Control with Git](http://swcarpentry.github.io/git-novice/)
* [The Unix Shell](http://swcarpentry.github.io/shell-novice/)

### General guidelines

We follow the [git pull request workflow](http://www.asmeurer.com/git-workflow/) to
make changes to our codebase.
Every change made to the codebase goes through a pull request so that our
[continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) services
have a chance to check that the code is up to standards and passes all our tests.
This way, the *main* branch is always stable.

General guidelines for pull requests (PRs):

* **Open an issue first** describing what you want to do. If there is already an issue
  that matches your PR, leave a comment there instead to let us know what you plan to
  do.
* Each pull request should consist of a **small** and logical collection of changes.
* Larger changes should be broken down into smaller components and integrated
  separately.
* Bug fixes should be submitted in separate PRs.
* Describe what your PR changes and *why* this is a good thing. Be as specific as you
  can. The PR description is how we keep track of the changes made to the project over
  time.
* Write descriptive commit messages. Chris Beams has written a
  [guide](https://chris.beams.io/posts/git-commit/) on how to write good commit
  messages.
* Be willing to accept criticism and work on improving your code; we don't want to break
  other users' code, so care must be taken not to introduce bugs.
* Be aware that the pull request review process is not immediate, and is generally
  proportional to the size of the pull request.

### Fork the repository

On the github page, first fork the repository to get your own version of it. This is with the `fork` button at the top of the GitHub repository page.

### Clone the repository

Now you need to get the cloned repository files onto your computer. This is referred to as `cloning`. In a terminal, or Git Bash, `cd` to the directory you want your cloned folder to be placed into and enter:
```bash
git clone https://github.com/organizationname/projectname
```

Now we need to configure Git to sync this fork to the main repository, not your fork of it.

`cd` into the directory you just cloned and run:

```bash
git remote add upstream https://github.com/organizationname/projectnamee.git
```

### Setting up `nox`

Most of the commands used in the development of `projectname` use the tool `nox`.
The `nox` commands are defined in the file [`noxfile.py`](https://github.com/organizationname/projectname/blob/main/noxfile.py), and are run in the terminal / command prompt with the format ```nox -s <<command name>>```.

You can install nox with `pip install nox`.

### Setting up your environment

Run the following `make` command to create a new environment and install the package dependencies. If you don't have / want to install make, just copy the commands from the Makefile file and run them in the terminal.

```
make create
```
Activate the environment:
```
mamba activate projectname
```
Install your local version:
```
make install
```
This environment now contains your local, editable version of projectname, meaning if you alter code in the package, it will automatically include those changes in your environment (you may need to restart your kernel if using Jupyter). If you need to update the dependencies, see the [update the dependencies](#update-the-dependencies) section below.

> **Note:** You'll need to activate the environment every time you start a new terminal.

### Make a branch

Instead of editing the main branch, which should remain stable, we create a `branch` and edit that. To create a new branch, called `new-branch` use the following command:

```bash
git checkout -b new-branch
```

### Make your changes

Now your ready to make your changes! Make sure to read the below sections to see how to correctly format and style your code contributions.


#### Code style and linting

We use [pre-commit](https://pre-commit.com/) to check code style. This can be used locally, by installing pre-commit, or can be used as a pre-commit hook, where it is automatically run by git for each commit to the repository. This pre-commit hook won't add or commit any changes, but will just inform your of what should be changed. Pre-commit is setup within the `.pre-commit-config.yaml` file. There are lots of hooks (processes) which run for each pre-commit call, including [Ruff](https://docs.astral.sh/ruff/) to format and lint the code. This allows you to not think about proper indentation, line length, or aligning your code during development. Before committing, or periodically while you code, run the following to automatically format your code:
```
nox -s lint
```

To have `pre-commit` run automatically on commits, install it with `pre-commit install`

Go through the output of this and try to change the code based on the errors. Search the error codes on the [Ruff documentation](https://docs.astral.sh/ruff/), which should give suggestions. Re-run the check to see if you've fixed it. Somethings can't be resolved (unsplittable urls longer than the line length). For these, add `# noqa: []` at the end of the line and the check will ignore it. Inside the square brackets add the specific error code you want to ignore.

We also use [Pylint](https://pylint.readthedocs.io/en/latest/), which performs static-linting on the code. This checks the code and catches many common bugs and errors, without running any of the code. This check is slightly slower the the `Ruff` check. Run it with the following:
```
nox -s pylint
```
Similar to using `Ruff`, go through the output of this, search the error codes on the [Pylint documentation](https://pylint.readthedocs.io/en/latest/) for help, and try and fix all the errors and warnings. If there are false-positives, or your confident you don't agree with the warning, add ` # pylint: disable=` at the end of the lines, with the warning code following the `=`.

To run both pre-commit and pylint together use:
```
nox -s style
```

#### Docstrings

**All docstrings** should follow the
[numpy style guide](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard).
All functions/classes/methods should have docstrings with a full description of all
arguments and return values.

While the maximum line length for code is automatically set by *Ruff*, docstrings
must be formatted manually. To play nicely with Jupyter and IPython, **keep docstrings
limited to 88 characters** per line. We don't have a good way of enforcing this
automatically yet, so please do your best.

#### Type hints

We have also opted to use type hints throughout the codebase. This means each function/class/method should be fulled typed, including the docstrings. We use [mypy](https://mypy.readthedocs.io/en/stable/) as a type checker.

Try and address all the errors and warnings. If there are complex types, just use `typing.Any`, or if necessary, ignore the line causing the issue by adding `# type: ignore[]` with the error code inside the square brackets.

#### Logging

When writing code; use logging (instead of print) to inform users of info, errors, and warnings. In each module `.py` file, import the project-wide logger instance with `from projectname import logger` and then for example: `logger.info("log this message")`

### Testing your code

Automated testing helps ensure that our code is as free of bugs as it can be.
It also lets us know immediately if a change we make breaks any other part of the code.

All of our test code and data are stored in the `tests` folder.
We use the [pytest](https://pytest.org/) framework to run the test suite, and our continuous integration systems with GitHub Actions use CodeCov to display how much of our code is covered by the tests.

Please write tests for your code so that we can be sure that it won't break any of the
existing functionality.
Tests also help us be confident that we won't break your code in the future.

If you're **new to testing**, see existing test files for examples of things to do.
**Don't let the tests keep you from submitting your contribution!**
If you're not sure how to do this or are having trouble, submit your pull request
anyway.
We will help you create the tests and sort out any kind of problem during code review.

Run the tests and calculate test coverage using:
```
nox -s test
```
To run a specific test by name:
```
pytest --cov=. -k "test_name"
```
The coverage report will let you know which lines of code are touched by the tests.
**Strive to get 100% coverage for the lines you changed.**
It's OK if you can't or don't know how to test something.
Leave a comment in the PR and we'll help you out.

### Documentation

The Docs are build with [Sphinx](https://www.sphinx-doc.org/en/master/) and hosted on [GitHub Pages](https://pages.github.com/).

> **Note:** The docs are automatically built on each commit to a PR, but if you've made significant changes to the docs its good practice to build them manually before a PR, to check them for errors.

#### Check the build manually (optional)

You can build the docs using:
```bash
    nox -s build_api_docs
```

```bash
    nox -s docs
```

Click the link to open your docs in a website which will automatically update as you make edits.

#### Automatically build the docs

Add, commit, and push all changes to GitHub in a Pull Request, and the docs should automatically be updated. If the PR can from the same repository (not a fork), then a preview of the updated docs should be available after a few minutes.

### Committing changes

Once your have made your changes to your branch of your forked repository, you'll need to commit the changes to your remote fork.

This can be done interactively, if you use a editor like `VS Code`, or in the terminal.

Stage your changes for a file:
```bash
git add <file>
```
or for a whole directory

```bash
git add <directory>
```

Then commit those staged changes:
```bash
git commit -m "a short description of your changes"
```

### Push your changes

With 1 or more committed changes, we can push those changes to your remote fork on GitHub.

```bash
git push -u origin your-branch-name
```

### Open a PR

Now in the original repository (not your fork), you can open a Pull-Request to incorporate your branch into the main repository. This is done on the main repository's GitHub page, using the Pull Request tab.

### Code review

After you've submitted a pull request, you should expect to hear at least a comment
within a couple of days.
We may suggest some changes or improvements or alternatives.

Some things that will increase the chance that your pull request is accepted quickly:

* Write a good and detailed description of what the PR does.
* Write tests for the code you wrote/modified.
* Readable code is better than clever code (even with comments).
* Write documentation for your code (docstrings) and leave comments explaining the
  *reason* behind non-obvious things.
* Include an example of new features in the gallery or tutorials.
* Follow the [numpy guide](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)
  for documentation.
* Run the automatic code formatter and style checks.

If you're PR involves changing the package dependencies, see the below instructions for [updating the dependencies](#update-the-dependencies).

Pull requests will automatically have tests run by GitHub Actions.
This includes running both the unit tests as well as code linters.
GitHub will show the status of these checks on the pull request.
Try to get them all passing (green).
If you have any trouble, leave a comment in the PR or
[post on the GH discussions page](https://github.com/organizationname/projectname/discussions).

### Sync your fork and local

Once the PR is merged, you will need to sync both your forked repository (origin) and your local clones repository with the following git commands:

```bash
git fetch upstream
git checkout main
git branch -d your-branch-name (OPTIONAL)
git merge upstream/main
git push origin main
```
Now both your forked (upstream) and local repositories are sync with the upstream repository where the PR was merged.

## Publish a new release

This will almost always be done by the developers, but as a guide for them, here are instructions on how to release a new version of the package.

Follow all the above instructions for formatting. Push your changes to a new or existing Pull Request. Once the automated GitHub Actions run (and pass), merge the PR into the main branch.

### PyPI (pip)
PyPI release are made automatically via GitHub actions whenever a pull request is merged.

### Conda-Forge
Once the new version is on PyPI, within a few hours a bot will automatically open a new PR in the [projectname conda-forge feedstock](https://github.com/conda-forge/projectname-feedstock). Go through the checklist on the PR. Most of the time the only actions needs are updated any changes made to the dependencies since the last release. Merge the PR and the new version will be available on conda-forge shortly.

Once the new version is on conda, update the binder .yml file, as below.

## Update the dependencies

To add or update a dependencies, add it to `pyproject.toml` either under `dependencies` or `optional-dependencies`. This will be included in the next build uploaded to PyPI.

If you add a dependency necessary for using the package, make sure to add it to the Binder config file and update the `environment.yml` file in the repository. See below.
