# Generated by Django 3.1.5 on 2021-06-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hami_projects', '0013_remove_project_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='عنوان مدیریتی'),
        ),
    ]