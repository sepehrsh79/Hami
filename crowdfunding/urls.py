# from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls.conf import include
from crowdfunding import settings
from .views import home_page

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home_page),
    path('projects/', include('projects.urls')),
    path('account/', include('account.urls')),
    path('support/', include('supports.urls')),
    path('site/', include('setting.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
