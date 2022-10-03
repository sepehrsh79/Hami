# Generated by Django 3.1.5 on 2021-06-09 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0012_branch_identifier_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='identifier_code',
            field=models.IntegerField(verbose_name='کد معرف شاخه'),
        ),
        migrations.AlterField(
            model_name='subbranches',
            name='sub_branche_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='زیر شاخه'),
        ),
    ]