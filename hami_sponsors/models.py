from django.db import models
from hami_projects.models import Project

class Sponsor (models.Model):
    fname = models.CharField(max_length=25,verbose_name='نام')
    lname = models.CharField(max_length=25,verbose_name=' نام خانوادگی')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='پروژه')
    phone = models.PositiveIntegerField(verbose_name='شماره تماس')
    address = models.CharField(max_length=100, verbose_name='آدرس')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'حامی پروژه'
        verbose_name_plural = 'حامیان پروژه'

    def __str__(self):
        return self.lname