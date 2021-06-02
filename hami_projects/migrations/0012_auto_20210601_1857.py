# Generated by Django 3.1.5 on 2021-06-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hami_projects', '0011_project_currentـbudget'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='عکس '),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('enable', 'فعال'), ('disable', 'غیر فعال')], max_length=35, verbose_name='وضعیت'),
        ),
    ]
