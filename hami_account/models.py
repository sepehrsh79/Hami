from django.db import models
from django.contrib.auth.models import User

class UserCustomize(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identifier_code = models.IntegerField(verbose_name='کد معرف', null=True, blank=True)

    class Meta:
        verbose_name = ''

    def __str__(self):
        return self.user.get_full_name()