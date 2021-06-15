from django.core import validators
from django.db import models
from hami_projects.models import Project
from django.contrib.auth.models import User

class Support (models.Model):
    title = models.CharField(max_length=25,verbose_name='عنوان', blank=True, null=True )
    price = models.FloatField(verbose_name='مبلغ حمایت')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='پروژه', blank=True, null=True)
    supporter = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='حمایت کننده', blank=True, null=True)
    date = models.DateField(max_length=100, verbose_name='تاریخ')

    class Meta:
        verbose_name = 'حمایت'
        verbose_name_plural = 'حمایت ها'

    def __str__(self):
        return self.title

class ExtraSupport(models.Model):
    price = models.FloatField(verbose_name='مبلغ جمع آوری شده')

    class Meta:
        verbose_name = 'بانک'
        verbose_name_plural = 'بانک حامی'

    def __str__(self):
        return str(self.price)

