from django.urls import path

from .views import support

urlpatterns = [
    path('support', support),
    # path('request', send_request, name='request'),
    # path('verify', verify , name='verify'),


]