from django.contrib import admin
from .models import Project, Comment, Group


@admin.register(Project)
class ProjectAdmin (admin.ModelAdmin):
    fieldsets = (
            ('اطلاعات', {'fields' : ('name', 'name_show','Groups', 'creator','discribtion', 'discribtion_show', 
            )}),
            ('وضعیت هزینه و زمان',{'fields' : ('budget', 'Currentـbudget','needed_time')}),
            ('ابزار ها',{'fields' : ('site', 'email', 'logo')}),
            ('وضعیت',{'fields' : ('status', 'order')}),
            )
    list_display = ('name', 'Groups', 'budget', 'status')


@admin.register(Comment)
class CommentAdmin (admin.ModelAdmin):
    list_display = ('name', 'date')

@admin.register(Group)
class GroupAdmin (admin.ModelAdmin):
    pass
