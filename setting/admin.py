from django.contrib import admin
from .models import SiteSetting, Slider


@admin.register(SiteSetting)
class CreatorAdmin (admin.ModelAdmin):
    pass


@admin.register(Slider)
class SliderAdmin (admin.ModelAdmin):
    pass
