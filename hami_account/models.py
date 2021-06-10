from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from hami_supports.models import Support

def find_subs_again(found_subbranch):
    subs = []
    lvl = 1
    for find in found_subbranch:
        u = find.sub_branche_user
        u_branch = Branch.objects.filter(head_branch=u).first()
        u_subbranchs = SubBranches.objects.filter(head_branch=u_branch)
        subs.extend(u_subbranchs)
    if subs:
        lvl = lvl + 1
        find_subs_again(subs)
    else:
        lvl = lvl
    return lvl


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

    #this function check how many sub branche is under this branch
    def get_sub_branches(self):
        count = self.subbranches_set.all()
        return len(count)

    #this function call get_subbranch_sups function from SubBeanches model to collect all of this branch supports
    def get_subbranch_total_support(self):
        total = 0
        subs = self.subbranches_set.all()
        for sub in subs:
            price = sub.get_subbranch_sups
            if price == None:
                price = 0
            else:
                price = sub.get_subbranch_sups

            total = total + price
        return total
    #this func will find how many sub branch levels are under this branch
    def get_subbranch_level(self):
        lvl = 0
        subbranchs = self.subbranches_set.all()
        if subbranchs.exists():
            lvl += 1
            for sub in subbranchs:
                add = sub.check_subbranch_exist()
                lvl = lvl + add
            return lvl
        else:
            return lvl

class SubBranches(models.Model):
    head_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='سر شاخه')
    sub_branche_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='زیر شاخه')

    class Meta:
        verbose_name = 'زیر شاخه'
        verbose_name_plural = 'زیر شاخه ها'

    def __str__(self):
        return self.sub_branche_user.get_full_name()

    #this function aggregate price field from all of this subbrach user supports
    @property
    def get_subbranch_sups(self):
        return self.sub_branche_user.support_set.all().aggregate(Sum('price'))['price__sum']

    def check_subbranch_exist(self):
        user = self.sub_branche_user
        found_branch = Branch.objects.filter(head_branch=user).first()
        found_subbranch = SubBranches.objects.filter(head_branch=found_branch)
        if found_subbranch:
            return find_subs_again(found_subbranch)
        else:
            return 0
