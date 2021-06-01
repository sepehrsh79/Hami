from django.contrib import admin
from .models import Reward, Project, Comment

class RewardInLine (admin.StackedInline):
    model = Reward
    extra = 1

@admin.register(Project)
class ProjectAdmin (admin.ModelAdmin):
    fieldsets = (
            ('اطلاعات', {'fields' : ('name', 'Groups', 'discribtion', 'place', 'logo')}),
            ('وضعیت هزینه و زمان',{'fields' : ('budget', 'needed_time')}),
            ('ابزار ها',{'fields' : ('site', 'email')}),
            ('وضعیت',{'fields' : ('status',)}),
            )
    list_display = ('name', 'Groups', 'budget', 'status')
    inlines = [RewardInLine]

@admin.register(Reward)
class RewardAdmin (admin.ModelAdmin):
    list_display = ('name', 'project', 'price', 'supports')

@admin.register(Comment)
class CommentAdmin (admin.ModelAdmin):
    list_display = ('name', 'date')
