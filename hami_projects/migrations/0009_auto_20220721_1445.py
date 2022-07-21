# Generated by Django 3.1.5 on 2022-07-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hami_projects', '0008_auto_20210616_0928'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='ProjectCategory',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Currentـbudget',
            new_name='current_budget',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='discribtion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='discribtion_show',
            new_name='description_show',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Groups',
            new_name='project_category',
        ),
        migrations.RenameField(
            model_name='projectcategory',
            old_name='discribtion',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='order',
        ),
        migrations.AlterField(
            model_name='project',
            name='needed_time',
            field=models.DateField(verbose_name='مدت زمان مورد نیاز'),
        ),
    ]
