# Generated by Django 3.1.5 on 2021-04-18 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countdown_core', '0004_auto_20210416_2359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countdown',
            old_name='love_reaction',
            new_name='like_reaction',
        ),
    ]
