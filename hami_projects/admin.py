from django.contrib import admin
from .models import Reward, Project, Comment, Group

class RewardInLine (admin.StackedInline):
    model = Reward
    extra = 1

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
    inlines = [RewardInLine]

@admin.register(Reward)
class RewardAdmin (admin.ModelAdmin):
    list_display = ('name', 'project', 'price', 'supports')

@admin.register(Comment)
class CommentAdmin (admin.ModelAdmin):
    list_display = ('name', 'date')

@admin.register(Group)
class GroupAdmin (admin.ModelAdmin):
    pass
