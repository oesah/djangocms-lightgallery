=====
Usage
=====

To use djangocms-lightgallery in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'djangocms_lightgallery.apps.DjangocmsLightgalleryConfig',
        ...
    )

Add djangocms-lightgallery's URL patterns:

.. code-block:: python

    from djangocms_lightgallery import urls as djangocms_lightgallery_urls


    urlpatterns = [
        ...
        url(r'^', include(djangocms_lightgallery_urls)),
        ...
    ]
