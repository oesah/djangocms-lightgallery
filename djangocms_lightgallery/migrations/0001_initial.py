# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 14:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LightGallery',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_lightgallery_lightgallery', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, verbose_name='light gallery title')),
                ('settings', jsonfield.fields.JSONField(blank=True, default=b'{}', help_text='Check <a href="http://sachinchoolur.github.io/lightGallery/docs/api.html" target="_blank">LightGallery Documentation</a> for possible settings <br>Use JSON format and check the errors in the editor<br>You can also use online JSON validators', null=True, verbose_name='light gallery settings')),
            ],
            options={
                'verbose_name': 'light gallery',
                'verbose_name_plural': 'light galleries',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='LightGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True, verbose_name='image link')),
                ('link_target', models.BooleanField(default=True, help_text='open link in new window', verbose_name='image link target')),
                ('caption_text', models.TextField(blank=True, null=True, verbose_name='caption text')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='lightgallery_images_filer', to=settings.FILER_IMAGE_MODEL, verbose_name='light gallery image')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='djangocms_lightgallery.LightGallery')),
            ],
            options={
                'verbose_name': 'light gallery image',
                'verbose_name_plural': 'light gallery images',
            },
        ),
    ]
