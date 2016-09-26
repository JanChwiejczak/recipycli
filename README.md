# Skeleton layout for recipy cli

[![Build Status](https://travis-ci.org/janhak/recipycli.svg?branch=master)](https://travis-ci.org/janhak/recipycli)

Sample skeleton layout for recipy cli. 
- Written in TDD style with 100% coverage against multiple versions of python
- Travis employed to automate testing 
- Tox to handle testing against different python versions.

To install clone this repo, start new virtualenv and run:
```
pip install -e .
```
requirements will be installed automatically. 

If you wish to run test you will need pytest and pytest-cov. Alternatively, you can only install tox and it will automatically install all required dependencies and python versions.