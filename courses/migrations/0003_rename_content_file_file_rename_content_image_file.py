# Generated by Django 4.0.4 on 2022-05-14 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_module_options_alter_course_subject_video_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='content',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='content',
            new_name='file',
        ),
    ]
