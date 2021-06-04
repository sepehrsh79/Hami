# Generated by Django 3.1.5 on 2021-06-04 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hami_supports', '0006_auto_20210604_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='supporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='حمایت کننده'),
        ),
    ]
