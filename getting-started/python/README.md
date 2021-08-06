[//]: # "Copyright Amazon.com Inc. or its affiliates. All Rights Reserved."
[//]: # "SPDX-License-Identifier: CC-BY-SA-4.0"

# Getting started with AWS Crypto Tools Python projects

This file introduces the various tools that we use in our Python projects
and how to get started developing on these projects.

## Tools

- All of our Python projects use [`tox`](https://tox.readthedocs.io/)
  to orchestrate all activity,
  both in CI and locally.
  Some common `tox` environments
  that should be in every project include:

  - `tox -e autoformat` : Applies all autoformatting rules.
  - `tox -e lint` : On most projects, this also runs `autoformat`.
  - `tox -e py{VERSION}-local` :
    Runs all non-integ tests using Python `VERSION`.
    (ex: `py38-local`)
  - `tox -e py{VERSION}-integ` :
    Runs all integ tests using Python `VERSION`.
    (ex: `py38-integ`)
    **NOTE: Integ tests usually require available AWS credentials.**
  - `tox -e py{VERSION}-all` :
    Runs all tests using Python `VERSION`.
    (ex: `py38-all`)
  - `tox -r -p {THREADS}` :
    Runs all default `tox` environments concurrently,
    `THREADS` at a time.
    Adjust `THREADS` as appropriate for your environment.
    (ex: `tox -r -p 7`)
  - `tox -e py38-accept,py38-examples,py38-integ,py38-local -p 3` :
    Runs the listed environments (here, all of `py38`) with 3 workers.
  
- We use [`pytest`](https://docs.pytest.org/) to run our tests.
- We use a variety of autoformatting and static analysis tools
  to ensure consistency among our projects.

  - [`black`](https://black.readthedocs.io/) :
    Applies general formatting requirements.
  - [`isort`](https://timothycrosley.github.io/isort/) :
    Sorts import statements.
  - [`flake8`](https://flake8.pycqa.org/) :
    Looks for code issues and inconsistencies
    (often partially overlaps with `pylint`).
    We also commonly use several `flake8` plugins:

    - [`flake8-isort`](https://github.com/gforcada/flake8-isort) :
      Looks for import statements
      that do not match our `isort` configuration.
    - [`flake8-print`](https://github.com/JBKahn/flake8-print) :
      Looks for print statements.
    - [`flake8-bugbear`](https://github.com/PyCQA/flake8-bugbear) :
      Looks for common bugs and design problems.
    - [`flake8-breakpoint`](https://github.com/afonasev/flake8-breakpoint) :
      Looks for breakpoints.
    - [`flake8-docstrings`](https://gitlab.com/pycqa/flake8-docstrings) :
      Applies `flake8` checks to docstrings.

  - [`pylint`](https://www.pylint.org/) :
    Looks for code issues and inconsistencies
    (often partially overlaps with `flake8`).
  - [`doc8`](https://github.com/pycqa/doc8) :
    Looks for issues in reStructuredText docs.
  - [`check-manifest`](https://github.com/mgedmin/check-manifest) :
    Looks for issues with `MANIFEST.in` file
    used for building source distributions.
  - [`bandit`](https://bandit.readthedocs.io/) :
    Looks for common security issues in Python code.
  - [`vulture`](https://github.com/jendrikseipp/vulture) :
    Looks for unused code.
    **NOTE: Vulture has a high false-positive rate for libraries
    but offers a useful perspective.**

## Local Development Setup

### Linux/MacOS

For local development,
we recommend using [`pyenv`](https://github.com/pyenv/pyenv).
If you want to quickly bootstrap a local development environment,
run:

```shell script
# "install" pyenv https://github.com/pyenv/pyenv#installation
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
# bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
# Install Python build dependencies
# (varies by OS)
# https://github.com/pyenv/pyenv/wiki#suggested-build-environment

# Install latest Python versions
for MINOR_VERSION in 2.7 3.5 3.6 3.7 3.8 3.9;do
  pyenv install $(pyenv install -l | grep "^  ${MINOR_VERSION}" | tail -1)
done

# set "local" pyenv version
#  just sets .python-version file in current directory
#  you can delete this afterwards
#
# This is the version of Python that all pipx-managed tools will use.
pyenv local $(pyenv versions --bare | grep 3.8 | tail -1)
# install pipx-in-pipx
# https://pipx-in-pipx.readthedocs.io/
pyenv exec pip install pipx-in-pipx
# remove pyenv local setting (optional)
rm .python-version
# restart shell to get all current and future pipx-managed binaries into path
exec "$SHELL"

# install tox
pipx install tox
pipx inject tox tox-pyenv
```

## `tox` tab completion
Given the number of `tox` environments, it can be very helpful to setup tab completion. 
For `zsh`, [here is a `tox` completion](https://github.com/zsh-users/zsh-completions/blob/master/src/_tox) compdef. 
The whole `zsh-completions` repo can be installed, or you can just download the `_tox` file and add it to your `fpath` before running `autoload -Uz compinit && compinit -i`.
