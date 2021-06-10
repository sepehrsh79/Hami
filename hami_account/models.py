from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from hami_supports.models import Support

class UserCustomize(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identifier_code = models.IntegerField(verbose_name='کد معرف')

    class Meta:
        verbose_name = ''

    def __str__(self):
        return self.user.get_full_name() 

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    User.add_to_class("__str__", get_full_name)


class Branch(models.Model):
    head_branch = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='سر شاخه')
    identifier_code = models.IntegerField(verbose_name='کد معرف شاخه')

    class Meta:
        verbose_name = 'شاخه'
        verbose_name_plural = 'شاخه ها'

    def __str__(self):
        return self.head_branch.get_full_name()

    def get_sub_branches(self):
        count = self.subbranches_set.all()
        return len(count)

    def get_subbranch_total_support(self):
        total = 0
        subs = self.subbranches_set.all()
        for sub in subs:
            total = total + sub.get_subbranch_sups
        return total

class SubBranches(models.Model):
    head_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='سر شاخه')
    sub_branche_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='زیر شاخه')

    class Meta:
        verbose_name = 'زیر شاخه'
        verbose_name_plural = 'زیر شاخه ها'

    def __str__(self):
        return self.sub_branche_user.get_full_name()
    @property
    def get_subbranch_sups(self):
        return self.sub_branche_user.support_set.all().aggregate(Sum('price'))['price__sum']
