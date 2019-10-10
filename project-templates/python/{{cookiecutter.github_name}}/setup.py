{{cookiecutter.derived.copyright_notice}}
"""{{cookiecutter.project_name}}."""
import io
import os
import re

from setuptools import find_packages, setup

VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*args):
    """Read complete file contents."""
    return io.open(os.path.join(HERE, *args), encoding="utf-8").read()


def get_version():
    """Read the version from this module."""
    init = read("src", "{{cookiecutter.module_name}}", "identifiers.py")
    return VERSION_RE.search(init).group(1)


def get_requirements():
    """Read the requirements file."""
    raw_requirements = read("requirements.txt")
    requirements = []
    dependencies = []

    for req in raw_requirements.splitlines():
        req = req.strip()
        if not req:
            continue
        elif req.startswith("#"):
            continue
        elif "+" in req:
            dependencies.append(req)
        else:
            requirements.append(req)

    return requirements, dependencies


install_requires, dependency_links = get_requirements()


setup(
    name="{{cookiecutter.pypi_name}}",
    version=get_version(),
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="{{cookiecutter.derived.github_url}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    maintainer="{{cookiecutter.author}}",
    description="{{cookiecutter.project_description}}",
    long_description=read("README.rst"),
    keywords="{{cookiecutter.pypi_keywords}}",
    data_files=["README.rst", "CHANGELOG.rst", "LICENSE", "requirements.txt"],
    license="{{cookiecutter.license}}",
    install_requires=install_requires,
    dependency_links=dependency_links,
    classifiers=[
        "Development Status :: {{cookiecutter.development_status}}",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        {%- if cookiecutter.license == "Apache 2.0" %}
        "License :: OSI Approved :: Apache Software License",
        {%- endif %}
        "Programming Language :: Python",
        {%- if cookiecutter.support_legacy_python == "yes" %}
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        {%- endif %}
        "Programming Language :: Python :: 3",
        {%- for version in cookiecutter.supported_modern_python_versions.split() %}
        "Programming Language :: Python :: {{version}}",
        {%- endfor %}
        "Programming Language :: Python :: Implementation :: CPython",
        {%- if cookiecutter.author_email == "aws-cryptools@amazon.com" %}
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        {%- endif %}
    ],
)
