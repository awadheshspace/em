# Generated by Django 5.1.5 on 2025-02-07 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exammantra', '0002_tag_practicepaper_userprofiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicepaper',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='practicepaper',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='userprofiles',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='PracticePaper',
        ),
        migrations.DeleteModel(
            name='UserProfiles',
        ),
    ]
