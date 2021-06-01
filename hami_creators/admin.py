from django.contrib import admin
from .models import Creator

@admin.register(Creator)
class CreatorAdmin (admin.ModelAdmin):
    list_display = ('name', 'id', 'phone')