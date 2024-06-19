# Generated by Django 3.2.7 on 2021-09-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samplesheets', '0017_update_jsonfields'),
    ]

    operations = [
        migrations.AddField(
            model_name='isatab',
            name='description',
            field=models.CharField(blank=True, help_text='Short description for ISA-Tab version (optional)', max_length=128, null=True),
        ),
    ]