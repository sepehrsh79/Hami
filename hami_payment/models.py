from django.db import models

from django.db import models
from hami_projects.models import Project

class Payment (models.Model):
    # sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت ها'

    def __str__(self):
        return str(self.sponsor.fname + self.sponsor.lname)