from django.urls import path 

from .views import (login_user,
    user_profile,
    admin_profile,
    logout_user,
    register_user,
    verify_user,
    create_group,
    edit_account,
    users_report )

urlpatterns = [
    path('account/user', user_profile),
    path('account/admin', admin_profile),
    path('account/admin/edit-groups', create_group),
    path('account/admin/users-report', users_report),
    path('account/login', login_user),
    path('account/logout', logout_user),
    path('account/register', register_user),
    path('account/verify', verify_user),
    path('account/edit', edit_account),
]