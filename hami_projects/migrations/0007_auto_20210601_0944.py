# Generated by Django 3.1.5 on 2021-06-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hami_projects', '0006_auto_20210601_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='discribtion_show',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='شرح قابل نمایش'),
        ),
        migrations.AddField(
            model_name='project',
            name='name_show',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='عنوان قابل نمایش'),
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='وزن'),
        ),
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.PositiveIntegerField(verbose_name='مبلغ مورد نیاز'),
        ),
        migrations.AlterField(
            model_name='project',
            name='discribtion',
            field=models.CharField(max_length=250, verbose_name='شرح مدیریتی'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=25, verbose_name='عنوان مدیریتی'),
        ),
        migrations.AlterField(
            model_name='project',
            name='needed_time',
            field=models.DateField(verbose_name='مدت زمان مورد نیاز '),
        ),
    ]
