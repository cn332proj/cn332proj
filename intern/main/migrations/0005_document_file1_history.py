# Generated by Django 3.2.6 on 2022-04-02 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220328_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('Document_ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Document_student_id', models.CharField(max_length=20, null=True)),
                ('Document_file1_id', models.CharField(max_length=200, null=True)),
                ('Document_file2_id', models.CharField(max_length=200, null=True)),
                ('Document_file3_id', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File1',
            fields=[
                ('File1_ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('File1_name', models.CharField(max_length=200, null=True)),
                ('File1_history_id', models.CharField(max_length=200, null=True)),
                ('File1_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('History_ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('History_student_id', models.CharField(max_length=20, null=True)),
                ('History_file_id', models.CharField(max_length=200, null=True)),
                ('History_admin_id', models.CharField(max_length=200, null=True)),
                ('History_file_type', models.CharField(max_length=1, null=True)),
                ('History_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
