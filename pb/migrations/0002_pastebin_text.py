# Generated by Django 5.1.4 on 2024-12-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastebin',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
