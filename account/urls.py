from django.urls import path

from . import views


urlpatterns = [
    path('account/user', views.user_profile),
    path('account/admin', views.admin_profile),
    path('account/admin/manage-category', views.create_edit_category),
    path('account/admin/<int:category_id>/edit-category', views.create_edit_category),
    path('account/admin/<int:category_id>/remove-category', views.remove_category),
    path('account/admin/manage-users', views.manage_users),
    path('account/admin/manage-supports', views.manage_supports),
    path('account/login', views.login_user),
    path('account/logout', views.logout_user),
    path('account/register', views.register_user),
    path('account/verify', views.verify_user),
    path('account/edit', views.edit_account),
    path('account/change-password', views.change_password),
    path('account/verify-change-password', views.verify_change_password),
    path('account/<int:user_id>/change-role', views.change_user_role),
    path('account/<int:user_id>/remove', views.remove_user),
]
