# Generated by Django 3.1.5 on 2021-06-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hami_projects', '0003_auto_20210601_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='leader',
        ),
        migrations.AlterField(
            model_name='project',
            name='Groups',
            field=models.CharField(choices=[('game', 'بازی'), ('book', 'کتاب'), ('cosial', 'اجتماعی')], max_length=35, verbose_name='دسته بندی'),
        ),
    ]
