from django.urls import path

from .views import support, general_support

urlpatterns = [
    path('support/', support),
    path('general-support/', general_support),
    # path('request', send_request, name='request'),
    # path('verify', verify , name='verify'),


]