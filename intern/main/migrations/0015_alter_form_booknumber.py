# Generated by Django 3.2.9 on 2022-04-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_form_booknumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='booknumber',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
    ]
