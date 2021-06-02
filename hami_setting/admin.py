from django.contrib import admin
from .models import SiteSetting

@admin.register(SiteSetting)
class CreatorAdmin (admin.ModelAdmin):
    pass