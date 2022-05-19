# Generated by Django 4.0.4 on 2022-05-14 14:45

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_content_options_alter_module_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(blank=True, verbose_name=['module']),
        ),
        migrations.AlterField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, verbose_name=['course']),
        ),
    ]
