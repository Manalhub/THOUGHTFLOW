# Generated by Django 5.0.6 on 2024-05-25 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_post_slug_post_slg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slg',
            new_name='slug',
        ),
    ]