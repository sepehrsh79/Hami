from django.urls import path

from . import views


urlpatterns = [
    path('user', views.user_profile),
    path('admin', views.admin_profile),
    path('admin/manage-category', views.create_edit_category),
    path('admin/<int:category_id>/edit-category', views.create_edit_category),
    path('admin/<int:category_id>/remove-category', views.remove_category),
    path('admin/manage-users', views.manage_users),
    path('admin/manage-supports', views.manage_supports),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('register', views.register_user),
    path('verify', views.verify_user),
    path('edit', views.edit_account),
    path('change-password', views.change_password),
    path('verify-change-password', views.verify_change_password),
    path('<int:user_id>/change-role', views.change_user_role),
    path('<int:user_id>/remove', views.remove_user),
]
