from django.db import models


class SiteSetting(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان سایت', null=True, blank=True)
    address = models.CharField(max_length=400, verbose_name='آدرس', null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name='تلفن', null=True, blank=True)
    mobile = models.CharField(max_length=50, verbose_name='تلفن همراه', null=True, blank=True)
    fax = models.CharField(max_length=50, verbose_name='فکس', null=True, blank=True)
    email = models.EmailField(max_length=50, verbose_name='ایمیل', null=True, blank=True)
    about_us = models.TextField(verbose_name='درباره ', null=True, blank=True)
    copy_right = models.CharField(verbose_name='متن کپی رایت', null=True, blank=True, max_length=200)
    logo_image = models.ImageField(upload_to='logo/', null=True, blank=True, verbose_name='تصویر لوگو')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = ' تنظیمات'

    def __str__(self):
        return self.title or " "


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to='', null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title or " "
