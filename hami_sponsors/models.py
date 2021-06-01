from django.db import models
from hami_projects.models import Project

class Sponsor (models.Model):
    name = models.CharField(max_length=25,verbose_name='نام و نام خانوادگی')
    card_id = models.PositiveIntegerField(verbose_name='کدملی')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='پروژه', null=True, blank=True)
    phone = models.PositiveIntegerField(verbose_name='شماره تماس')
    address = models.CharField(max_length=100, verbose_name='آدرس')
    Postalـcode = models.PositiveIntegerField(verbose_name='کد پستی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'حامی پروژه'
        verbose_name_plural = 'حامیان پروژه'

    def __str__(self):
        return self.name