# Generated by Django 5.0.4 on 2024-04-28 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_youtube_iframe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtube',
            name='iframe',
        ),
    ]
