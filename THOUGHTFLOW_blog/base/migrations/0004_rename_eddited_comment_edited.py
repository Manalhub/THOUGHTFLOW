# Generated by Django 5.0.6 on 2024-05-26 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_slg_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='eddited',
            new_name='edited',
        ),
    ]
