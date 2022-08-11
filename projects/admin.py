from django.contrib import admin
from .models import Project, Comment, ProjectCategory


@admin.register(Project)
class ProjectAdmin (admin.ModelAdmin):
    fieldsets = (
            ('اطلاعات', {'fields': ('name', 'name_show', 'project_category', 'creator', 'description', 'description_show', )}),
            ('وضعیت هزینه و زمان', {'fields': ('budget', 'current_budget', 'needed_time')}),
            ('ابزار ها', {'fields': ('site', 'email', 'logo')}),
            ('وضعیت', {'fields': ('status', 'order')}),
            )
    list_display = ('name', 'project_category', 'budget', 'status')


@admin.register(Comment)
class CommentAdmin (admin.ModelAdmin):
    list_display = ('name', 'date')


@admin.register(ProjectCategory)
class GProjectCategoryAdmin (admin.ModelAdmin):
    pass
