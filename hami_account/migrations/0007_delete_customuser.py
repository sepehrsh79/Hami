# Generated by Django 3.1.5 on 2021-06-04 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hami_supports', '0007_auto_20210604_1955'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('hami_account', '0006_auto_20210604_1955'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
