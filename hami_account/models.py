from django.db import models
from django.contrib.auth.models import User

class UserCustomize(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identifier_code = models.IntegerField(verbose_name='کد معرف', null=True, blank=True)

    class Meta:
        verbose_name = ''

    def __str__(self):
        return self.user.get_full_name() 

class SubBranches(models.Model):
    head_branch = models.ForeignKey(User, related_name="head", on_delete=models.CASCADE, verbose_name='سر شاخه', null=True, blank=True )
    sub_branch_user = models.ForeignKey(User, related_name="sub", on_delete=models.CASCADE, verbose_name='زیر شاخه')

    class Meta:
        verbose_name = 'زیر شاخه'
        verbose_name_plural = 'زیر شاخه ها'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    User.add_to_class("__str__", get_full_name)

    def __str__(self):
        return self.sub_branch_user.get_full_name()