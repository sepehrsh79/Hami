from django.urls import path

from . import views


urlpatterns = [
    path('setting', views.site_setting_edit),
    path('slider', views.site_slider),
    path('slider/<int:slider_id>/delete', views.remove_slider),
]
