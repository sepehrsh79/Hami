# Generated by Django 3.1.5 on 2021-06-11 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hami_sliders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='description',
        ),
    ]
