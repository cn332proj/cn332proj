# Generated by Django 3.2.9 on 2022-04-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_form_nametitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='nameTitle',
            field=models.CharField(choices=[('นางสาว', 'Miss'), ('นาง', 'Mrs'), ('นาย', 'Mr')], default=None, max_length=100),
        ),
    ]