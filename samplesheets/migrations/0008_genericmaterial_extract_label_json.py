# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-12 12:23
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


def populate_extract_label_json(apps, schema_editor):
    """Populate new JSON extract label field based on values in old field"""
    GenericMaterial = apps.get_model('samplesheets', 'GenericMaterial')

    for material in GenericMaterial.objects.all():
        if material.extract_label:
            material.extract_label_json = {'value': material.extract_label}
            material.save()


class Migration(migrations.Migration):

    dependencies = [
        ('samplesheets', '0007_altamisa_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericmaterial',
            name='extract_label_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Extract label (JSON)', null=True),
        ),
        migrations.RunPython(populate_extract_label_json)
    ]
