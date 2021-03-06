# Generated by Django 3.2.9 on 2022-05-31 16:34

from django.db import migrations, models
import main.utils
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_form_booknumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentstep4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('attachment', models.FileField(null=True, upload_to=main.utils.upload_to, validators=[main.validators.validate_file_extension])),
            ],
        ),
    ]
