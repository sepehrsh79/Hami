# Generated by Django 3.1.5 on 2021-06-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hami_projects', '0006_auto_20210614_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('enable', 'فعال'), ('disable', 'غیر فعال')], default='disable', max_length=35, verbose_name='وضعیت'),
        ),
    ]
