# Generated by Django 4.1.5 on 2023-10-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_share', '0018_alter_codes_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='codes',
            name='is_spam',
            field=models.BooleanField(default=False),
        ),
    ]
