# Generated by Django 3.1.5 on 2021-06-01 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hami_supports', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sponsor',
            new_name='Support',
        ),
    ]