# Generated by Django 3.1.5 on 2021-06-09 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hami_account', '0003_auto_20210609_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subbranches',
            name='head_branch',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='head', to=settings.AUTH_USER_MODEL, verbose_name='سر شاخه'),
        ),
        migrations.AlterField(
            model_name='subbranches',
            name='sub_branch_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to=settings.AUTH_USER_MODEL, verbose_name='زیر شاخه'),
        ),
    ]
