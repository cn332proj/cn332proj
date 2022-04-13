# Generated by Django 4.0.3 on 2022-04-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_merge_20220404_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='dowloadForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='File1',
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]
