#!/usr/bin/env python
# -*- coding: utf-8 -*-
from djangocms_helper.base_test import BaseTestCase
from django.test.client import RequestFactory

from sekizai.context import SekizaiContext

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from djangocms_lightgallery.cms_plugins import LightGalleryPlugin
from djangocms_lightgallery.apps import DjangocmsLightgalleryConfig

from ._factories import LightGalleryImageFactory, LightGalleryFactory


class LightGalleryPluginTests(BaseTestCase):

    def create_images(self, gallery):
        for n in range(1, 7):
            image = self.create_filer_image_object()
            gallery_image = LightGalleryImageFactory.create(
                id=n,
                image=image,
                gallery_id=gallery.id)
            self.assertEqual(str(gallery_image), "test_file.jpg")

    def setUp(self):
        self.app = DjangocmsLightgalleryConfig
        self.gallery = LightGalleryFactory.create()
        self.create_images(self.gallery)

    def test_plugin_basics(self):
        self.assertEqual(self.app.name, 'djangocms_lightgallery')

    def test_plugin_html(self):
        # create plugin in placeholder
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            LightGalleryPlugin,
            'de'
        )
        model_instance.copy_relations(self.gallery)

        # render plugin
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(model_instance, SekizaiContext())

        # do some testing with rendered html
        self.assertIn('class="lg-gallery"', html)
        self.assertIn('id="lightgallery-%s' % model_instance.id, html)
