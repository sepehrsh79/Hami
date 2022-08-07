from django.urls import path

from . import views


urlpatterns = [
    path('site/setting', views.site_setting_edit),
    path('site/slider', views.site_slider),
    path('site/slider/<int:slider_id>/delete', views.remove_slider),
]
