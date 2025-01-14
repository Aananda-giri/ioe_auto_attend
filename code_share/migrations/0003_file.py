# Generated by Django 4.1.5 on 2023-07-08 09:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_share', '0002_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=25)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('file_path', models.FileField(upload_to='files/')),
                ('drive_links', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(blank=True, null=True), size=None)),
            ],
        ),
    ]
