from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# add a new User admin to old user admin
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'is_staff', 'last_login']


# Re-register UserAdmin and unregister old user admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
