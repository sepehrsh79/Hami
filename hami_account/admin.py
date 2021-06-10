from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from hami_account.models import UserCustomize, SubBranches, Branch


class EmployeeInline(admin.StackedInline):
    model = UserCustomize
    can_delete = False
    verbose_name_plural = 'اطلاعات بیشتر'

# add a new User admin to old user admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)
    list_display = ['username', 'first_name', 'last_name', 'is_staff', 'last_login']

# Re-register UserAdmin and unregister old user admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Branch)
class BranchAdmin (admin.ModelAdmin):
    list_display = ('head_branch',)

@admin.register(SubBranches)
class SubBranchesAdmin (admin.ModelAdmin):
    list_display = ('sub_branche_user', 'head_branch')

