# Generated by Django 2.1.9 on 2019-06-25 19:12

import mimetypes

from django.db import migrations, models

import filer.models.filemodels


def guess_mimetypes(apps, schema_editor):
    FileModel = apps.get_model('filer', 'File')
    for file_obj in FileModel.objects.all():
        file_obj.mime_type, _ = mimetypes.guess_type(file_obj.file.url)
        file_obj.save(update_fields=['mime_type'])


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0011_auto_20190418_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='mime_type',
            field=models.CharField(default='application/octet-stream', help_text='MIME type of uploaded content', max_length=255, validators=[filer.models.filemodels.mimetype_validator]),
        ),
        migrations.RunPython(guess_mimetypes, reverse_code=migrations.RunPython.noop),
    ]