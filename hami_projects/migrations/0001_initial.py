# Generated by Django 3.1.5 on 2021-06-08 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('slug', models.CharField(blank=True, max_length=120, null=True, verbose_name='عنوان مدیریتی')),
                ('discribtion', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='عکس ')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True, verbose_name='عنوان مدیریتی')),
                ('name_show', models.CharField(max_length=25, verbose_name='عنوان قابل نمایش')),
                ('discribtion', models.TextField(blank=True, max_length=250, null=True, verbose_name='شرح مدیریتی')),
                ('discribtion_show', models.TextField(max_length=250, verbose_name='شرح قابل نمایش')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='وزن')),
                ('budget', models.PositiveIntegerField(verbose_name='مبلغ مورد نیاز')),
                ('Currentـbudget', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='مبلغ جمع شده')),
                ('needed_time', models.DateField(verbose_name='مدت زمان مورد نیاز ')),
                ('site', models.CharField(max_length=35, verbose_name='سایت')),
                ('email', models.CharField(max_length=35, verbose_name='ایمیل')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='عکس کاور')),
                ('status', models.CharField(choices=[('enable', 'فعال'), ('disable', 'غیر فعال')], default='disable', max_length=35, verbose_name='وضعیت')),
                ('Groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hami_projects.group', verbose_name='دسته بندی')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='صاحب پروژه')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه ها',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='عنوان')),
                ('discribtion', models.CharField(max_length=250, verbose_name='شرح پاداش')),
                ('price', models.PositiveIntegerField(verbose_name='هزینه پاداش')),
                ('supports', models.PositiveIntegerField(verbose_name='حمایت ها')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hami_projects.project', verbose_name='پروژه مرتبط')),
            ],
            options={
                'verbose_name': 'پاداش',
                'verbose_name_plural': 'پاداش ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True, verbose_name='نام و نام خانوادگی')),
                ('subject', models.CharField(blank=True, max_length=25, null=True, verbose_name='عنوان')),
                ('message', models.CharField(max_length=250, verbose_name='متن پیام')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hami_projects.project', verbose_name='پروژه مرتبط')),
            ],
            options={
                'verbose_name': 'دیدگاه',
                'verbose_name_plural': 'دیدگاه ها',
            },
        ),
    ]
