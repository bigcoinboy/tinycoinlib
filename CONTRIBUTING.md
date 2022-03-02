# Contributing to TinyCoinLib

Thank you for considering to contribute to
TinyCoinLib.

This page is to help you out.


## Ways to contribute

### 1) Test it

Try to run the examples or integrate TinyCoinLib to your project.
This is especially useful for discovering software bugs.

### 2) Study its source code

TinyCoinLib (as the name implies) attempts to stay tiny so that as many people
as possible would have time to read its source code.
In addition, it is programmed using Python
that reads pretty much like plain English.

These factors make it relatively easy for anyone to audit TinyCoinLib
and confirm that it can be trusted.


### 3) Open an issue

If you have a bug report, questions, improvement ideas or similar,
please see if there already is an existing issue or open new.

Participating in [Issues](github.com/bigcoinboy/tinycoinlib/issues)
(maybe just to add your insight
or a comment) is highly appreciated.


### 4) Modify it

TinyCoinLib is free software, meaning (among other things) that you can
modify the program as you wish and redistribute it under the GPLv3 license.
This independent development is commonly referred as *forking*.

If you want to bring your changes back this project (highly appreciated),
please follow the coding guidelines given below.



## Coding guidelines for authors

- Generally, follow [PEP8](https://www.python.org/dev/peps/pep-0008/#comments)
- For comments, follow [numpy's style guide](https://numpydoc.readthedocs.io/en/latest/format.html).
For more, see [sphinx's numpy examples](https://www.sphinx-doc.org/en/master/usage/extensions/example_numpy.html).
- Avoid advanced or rarely used features of Python.
TinyCoinLib should be as understandable as possible for as many people as possible.
- Add no external dependencies (Python standard library only)

TinyCoinLib is meant to be tiny. For new features, it may be better to fork the project and
call it SmallCoinLib or HugeCoinLib, depending on the amount of features added.


## Git branches

- main for tested, "production" ready code
- develop for development

