from django.db import models

class Support (models.Model):
    name = models.CharField(max_length=25,verbose_name='نام و نام خانوادگی')
    card_id = models.PositiveIntegerField(verbose_name='کدملی')
    phone = models.PositiveIntegerField(verbose_name='شماره تماس')
    address = models.CharField(max_length=100, verbose_name='آدرس')
    Postalـcode = models.PositiveIntegerField(verbose_name='کد پستی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'پشتیبان'
        verbose_name_plural = 'پشتیبان ها'

    def __str__(self):
        return self.name