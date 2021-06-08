from django.db import models

class SiteSetting(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان سایت')
    address = models.CharField(max_length=400, verbose_name='آدرس')
    phone = models.CharField(max_length=50, verbose_name='تلفن')
    mobile = models.CharField(max_length=50, verbose_name='تلفن همراه')
    fax = models.CharField(max_length=50, verbose_name='فکس')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ', null=True, blank=True)
    copy_right = models.CharField(verbose_name='متن کپی رایت', null=True, blank=True, max_length=200)
    logo_image = models.ImageField(upload_to='logo/', null=True, blank=True, verbose_name='تصویر لوگو')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = ' تنظیمات'

    def __str__(self):
        return self.title or " "