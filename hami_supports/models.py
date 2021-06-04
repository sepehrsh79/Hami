from django.db import models
from hami_projects.models import Project
from django.contrib.auth.models import User

class Support (models.Model):
    title = models.CharField(max_length=25,verbose_name='عنوان' )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='پروژه')
    supporter = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='حمایت کننده')
    date = models.DateField(max_length=100, verbose_name='تاریخ')

    class Meta:
        verbose_name = 'حمایت'
        verbose_name_plural = 'حمایت ها'

    def __str__(self):
        return str(self.title)