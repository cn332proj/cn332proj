# Generated by Django 3.2.9 on 2022-03-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='pdf',
        ),
        migrations.AddField(
            model_name='company',
            name='link',
            field=models.URLField(null=True),
        ),
    ]
