# Generated by Django 4.1.2 on 2023-06-13 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0010_event_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nominee',
            old_name='nominee_picture',
            new_name='picture',
        ),
    ]
