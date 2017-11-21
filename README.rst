=============================
djangocms-lightgallery
=============================

.. image:: https://badge.fury.io/py/djangocms_lightgallery.svg
    :target: https://badge.fury.io/py/djangocms_lightgallery

.. image:: https://travis-ci.org/oesah/djangocms_lightgallery.svg?branch=master
    :target: https://travis-ci.org/oesah/djangocms_lightgallery

.. image:: https://codecov.io/gh/oesah/djangocms_lightgallery/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/oesah/djangocms_lightgallery

DjangoCMS Plugin for LighGallery library

Documentation
-------------

The full documentation is at https://djangocms_lightgallery.readthedocs.io.

Quickstart
----------

**Requirements**

* django-filer

Install djangocms-lightgallery::

    pip install djangocms_lightgallery

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'djangocms_lightgallery',
        ...
    )


Features
--------

* create image galleries with 

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
