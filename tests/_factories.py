#!/usr/bin/env python
# -*- coding: utf-8 -*-
import factory

from djangocms_lightgallery import models


class LightGalleryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LightGallery

    title = 'Test LightGallery'


class LightGalleryImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LightGalleryImage

    caption_text = 'Test Caption'
