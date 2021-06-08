from django.contrib import admin
from .models import Support

@admin.register(Support)
class SupportAdmin (admin.ModelAdmin):
    default_auto_field = 'django.db.models.AutoField'

    list_display = ('title', 'price', 'project', 'supporter', 'date')