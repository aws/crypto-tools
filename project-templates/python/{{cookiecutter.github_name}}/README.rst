{% for i in cookiecutter.pypi_name %}#{% endfor %}
{{cookiecutter.pypi_name}}
{% for i in cookiecutter.pypi_name %}#{% endfor %}

.. image:: https://img.shields.io/pypi/v/{{cookiecutter.pypi_name}}.svg
   :target: https://pypi.python.org/pypi/{{cookiecutter.pypi_name}}
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.pypi_name}}.svg
   :target: https://pypi.python.org/pypi/{{cookiecutter.pypi_name}}
   :alt: Supported Python Versions

.. image:: https://img.shields.io/badge/code_style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black

.. image:: https://readthedocs.org/projects/{{cookiecutter.pypi_name}}/badge/
   :target: https://{{cookiecutter.pypi_name}}.readthedocs.io/en/stable/
   :alt: Documentation Status

.. image:: https://travis-ci.org/{{cookiecutter.github_user}}/{{cookiecutter.github_name}}.svg?branch=master
   :target: https://travis-ci.org/{{cookiecutter.github_user}}/{{cookiecutter.github_name}}

.. image:: https://ci.appveyor.com/api/projects/status/REPLACEME/branch/master?svg=true
   :target: https://ci.appveyor.com/project/REPLACEME

{{cookiecutter.project_description}}

***************
Getting Started
***************

Required Prerequisites
======================

* Suported Python versions

{%- if cookiecutter.support_legacy_python == "yes" %}
  * 2.7
{%- endif %}
{%- for version in cookiecutter.supported_modern_python_versions.split() %}
  * {{version}}
{%- endfor %}

Installation
============

.. code::

   $ pip install {{cookiecutter.pypi_name}}

***********
Development
***********

Prerequisites
=============

* Required

  * Python 3.6+
  * `tox`_ : We use tox to drive all of our testing and package management behavior.
    Any tests that you want to run should be run using tox.

* Optional

  * `pyenv`_ : If you want to test against multiple versions of Python and are on Linux or MacOS,
    we recommend using pyenv to manage your Python runtimes.
  * `tox-pyenv`_ : Plugin for tox that enables it to use pyenv runtimes.
  * `detox`_ : Parallel plugin for tox. Useful for running a lot of test environments quickly.

Setting up pyenv
----------------

If you are using pyenv, make sure that you have set up all desired runtimes and configured the environment
before attempting to run any tests.

1. Install all desired runtimes.

   * ex: ``pyenv install 3.7.0``
   * **NOTE:** You can only install one runtime at a time with the ``pyenv install`` command.

1. In the root of the checked out repository for this package, set the runtimes that pyenv should use.

   * ex: ``pyenv local 2.7.14 3.4.6 3.5.3 3.6.4 3.7.0``
   * **NOTE:** This creates the ``.python-version`` file that pyenv will use. Pyenv treats the first
     version in that file as the default Python version.


Running tests
=============

There are two criteria to consider when running our tests:
what version of Python do you want to use and what type of tests do you want to run?

For a full listing of the available types of tests available,
see the ``[testenv]commands`` section of the ``tox.ini`` file.

All tests should be run using tox.
To do this, identify the test environment that you want tox to run using the ``-e ENV_NAME`` flag.
The standard test environments are named as a combination of the Python version
and the test type in the form ``VERSION-TYPE``.
For example, to run the ``local`` tests against CPython 3.7:

.. code-block:: bash

    tox -e py37-local

If you want to provide custom parameters to pytest to manually identify what tests you want to run,
use the ``manual`` test type. Any arguments you want to pass to pytest must follow the ``--`` argument.
Anything before that argument is passed to tox. Everything after that argument is passed to pytest.

.. code-block:: bash

    tox -e py37-manual -- test/unit/test_example_file.py

Before submitting a pull request
================================

Before submitting a pull request, please run the ``lint`` tox environment.
This will ensure that your submission meets our code formatting requirements
and will pass our continous integration code formatting tests.


*****
Usage
*****

REPLACEME

.. _tox: http://tox.readthedocs.io/
.. _detox: https://pypi.org/project/detox/
.. _tox-pyenv: https://pypi.org/project/tox-pyenv/
.. _pyenv: https://github.com/pyenv/pyenv
