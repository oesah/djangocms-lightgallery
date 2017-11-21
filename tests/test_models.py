#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_djangocms_lightgallery
------------

Tests for `djangocms_lightgallery` models module.
"""

from djangocms_helper.base_test import BaseTestCase as CMSBaseTestCase

from djangocms_lightgallery import models


class TestDjangocms_lightgallery(CMSBaseTestCase):

    def setUp(self):
        self.gallery = models.LightGallery.objects.create()
        for i in range(1, 11):
            image = models.LightGalleryImage()
            image.gallery = self.gallery
            image.image = self.create_filer_image_object()
            image.save()

    def test_model_str(self):
        self.assertEqual(str(self.gallery), self.gallery.title)
        self.assertEqual(
            str(self.gallery.images.last()),
            self.gallery.images.last().image.original_filename)

    def tearDown(self):
        pass
