# Generated by Django 3.2.6 on 2021-12-18 05:02

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('code_share', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('author', models.CharField(default='', max_length=80)),
                ('email', models.EmailField(default='', max_length=254)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('branch_name', models.CharField(default='', max_length=20)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=150), default=None, null=True, size=None)),
                ('valid_email', models.BooleanField(default=True)),
                ('hide_code', models.BooleanField(default=False)),
                ('originalCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code_share.code')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]