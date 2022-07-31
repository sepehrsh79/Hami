from django.urls import path

from .views import (login_user,
                    user_profile,
                    admin_profile,
                    logout_user,
                    register_user,
                    verify_user,
                    create_group,
                    edit_account,
                    change_password,
                    manage_users,
                    manage_supports
                    )

urlpatterns = [
    path('account/user', user_profile),
    path('account/admin', admin_profile),
    path('account/admin/edit-groups', create_group),
    path('account/admin/manage-users', manage_users),
    path('account/admin/manage-supports', manage_supports),
    path('account/login', login_user),
    path('account/logout', logout_user),
    path('account/register', register_user),
    path('account/verify', verify_user),
    path('account/edit', edit_account),
    path('account/change-password', change_password),

]
