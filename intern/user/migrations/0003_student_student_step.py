# Generated by Django 3.2.6 on 2022-04-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220402_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Student_step',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
