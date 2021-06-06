from django.contrib import admin
from .models import Support

@admin.register(Support)
class SupportAdmin (admin.ModelAdmin):
    list_display = ('title', 'price', 'project', 'supporter', 'date')