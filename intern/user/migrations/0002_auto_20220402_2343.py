# Generated by Django 3.2.6 on 2022-04-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Student_ID',
            new_name='Student_department',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Student_password',
            new_name='Student_email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='no',
            new_name='Student_pk',
        ),
        migrations.AddField(
            model_name='student',
            name='Student_faculty',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Student_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Student_name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Student_name_th',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Student_prefix',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
