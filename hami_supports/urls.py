from django.urls import path

from .views import support, send_request, verify

urlpatterns = [
    path('support', support),
    path('request', send_request, name='request'),
    path('verify', verify , name='verify'),


]