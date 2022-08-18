# Generated by Django 3.1.5 on 2022-08-18 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20220818_0543'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('supports', '0008_auto_20220806_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='support',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.project', verbose_name='پروژه'),
        ),
        migrations.AlterField(
            model_name='support',
            name='supporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='حمایت کننده'),
        ),
    ]
