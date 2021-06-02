from django.db import models

class Support (models.Model):
    fname = models.CharField(max_length=25,verbose_name='نام')
    lname = models.CharField(max_length=25,verbose_name=' نام خانوادگی')
    phone = models.PositiveIntegerField(verbose_name='شماره تماس')
    address = models.CharField(max_length=100, verbose_name='آدرس')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'پشتیبان'
        verbose_name_plural = 'پشتیبان ها'

    def __str__(self):
        return self.name