# Generated by Django 3.1.5 on 2021-06-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hami_projects', '0005_auto_20210601_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.CharField(max_length=250, verbose_name='متن پیام'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='نام و نام خانوادگی'),
        ),
    ]