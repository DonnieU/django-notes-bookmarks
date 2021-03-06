# Generated by Django 2.0.6 on 2018-06-25 22:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookmark',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
