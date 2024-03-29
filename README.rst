=============================
djangocms-lightgallery
=============================

.. image:: https://badge.fury.io/py/djangocms-lightgallery.svg
    :target: https://badge.fury.io/py/djangocms-lightgallery

.. image:: https://travis-ci.org/oesah/djangocms-lightgallery.svg?branch=master
    :target: https://travis-ci.org/oesah/djangocms-lightgallery

.. image:: https://codecov.io/gh/oesah/djangocms-lightgallery/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/oesah/djangocms-lightgallery

DjangoCMS Plugin for `LightGallery <http://sachinchoolur.github.io/lightGallery/>`_.

Documentation
-------------

The full documentation is at https://djangocms-lightgallery.readthedocs.io.

Quickstart
----------

Requirements

* django-filer

Install djangocms-lightgallery::

    pip install djangocms-lightgallery

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'djangocms_lightgallery',
        ...
    )


Features
--------

* create image galleries with `lightGallery`
* displays images in gallery as a thumbnail preview


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
*  LightGallery_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _LightGallery: http://sachinchoolur.github.io/lightGallery/


ToDo
----

* make the thumbnail preview customizable
* give more styling options

Sponsorship
-----------

This project is maintained by `Mathison AG | Mobile & Web Development <https://mathison.ch>`_.

Used by
-------

* `Stella Gastro | The best Restaurants, Bars and Cafés in Switzerland <https://stellagastro.ch>`_.
* `Lancer Express | The Swiss Army Knife for Freelancers <https://my.lancer.express>`_.
