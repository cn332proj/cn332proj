# Generated by Django 4.0.3 on 2022-04-13 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_dowloadform_delete_document_delete_file1_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dowloadForm',
            new_name='Dowload',
        ),
    ]