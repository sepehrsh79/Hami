from django.db import models
from hami_projects.models import Project
from django.contrib.auth.models import User


class Support(models.Model):
    amount = models.FloatField(verbose_name='مبلغ حمایت')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='پروژه', blank=True, null=True)
    supporter = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='حمایت کننده')
    date = models.DateField(max_length=100, verbose_name='تاریخ')

    class Meta:
        verbose_name = 'حمایت'
        verbose_name_plural = 'حمایت ها'

    def __str__(self):
        return '{0} تومان حمایت از {1}'.format(self.amount, self.supporter if not None else 'ناشناس')

