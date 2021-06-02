# Generated by Django 3.1.5 on 2021-06-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hami_supports', '0002_auto_20210601_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='support',
            name='Postalـcode',
        ),
        migrations.RemoveField(
            model_name='support',
            name='card_id',
        ),
        migrations.RemoveField(
            model_name='support',
            name='name',
        ),
        migrations.AddField(
            model_name='support',
            name='fname',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='نام'),
        ),
        migrations.AddField(
            model_name='support',
            name='lname',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name=' نام خانوادگی'),
        ),
    ]
