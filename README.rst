.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/collective/codesyntax.login/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/codesyntax.login/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/codesyntax.login/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/codesyntax.login?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/codesyntax.login/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/codesyntax.login

.. image:: https://img.shields.io/pypi/v/codesyntax.login.svg
    :target: https://pypi.python.org/pypi/codesyntax.login/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/codesyntax.login.svg
    :target: https://pypi.python.org/pypi/codesyntax.login
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/codesyntax.login.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/codesyntax.login.svg
    :target: https://pypi.python.org/pypi/codesyntax.login/
    :alt: License


================
codesyntax.login
================

Add-on on to set login basics for CodeSyntax users

This product is meant to be used together with pas.plugins.oidc and, if wanted, collective.regenv.

It creates a user group for CodeSyntax users that will be authorized to log in in a Plone site using pas.plugins.oidc

Installation
------------

Install codesyntax.login by adding it to your buildout::

    [buildout]

    ...

    eggs =
        codesyntax.login


and then running ``bin/buildout``

Check pas.plugins.oidc documentation to learn how to configure it.


License
-------

The project is licensed under the GPLv2.
