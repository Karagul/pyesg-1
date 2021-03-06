"""Package setup"""
from setuptools import setup, find_packages


with open("README.md") as f:
    README = f.read()

setup(
    name="pyesg",
    version="0.1.2",
    description="Economic Scenario Generator for Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jason-ash/pyesg",
    author="Jason Ash",
    author_email="jason@ashanalytics.com",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "scipy"],
    extras_require={"dev": ["hypothesis", "pre-commit", "pylint", "mypy"]},
    include_package_data=True,
    package_data={
        "pyesg": ["../README.md", "../LICENSE.md", "../MANIFEST.in", "datasets/*"]
    },
    test_suite="tests",
    zip_safe=False,
)
