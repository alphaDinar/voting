# Generated by Django 4.1.2 on 2023-06-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0008_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True),
        ),
    ]