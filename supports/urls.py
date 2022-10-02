from django.urls import path

from .views import support, general_support

urlpatterns = [
    path('project-support/', support),
    path('general-support/', general_support),
]
