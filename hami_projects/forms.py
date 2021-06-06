from django import forms
from django.core import validators
from .models import Group, Project

groups_form = []

def add_group(n):
    groups = Group.objects.all()
    for group in groups:
        n += ((f'{group.slug}', f'{group.title}'),)
    return n

class CommentForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد نمایید','class': 'form-control'}),
        label='نام و نام خانوادگی',
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا موضوع پیام خود را وارد نمایید','class': 'form-control'}),
        label='موضوع',
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا متن پیام خود را وارد نمایید','class': 'form-control'}),
        label='دیدگاه شما'
    )


class CreateProject(forms.Form):

    name_show = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام پروژه خود را وارد نمایید', 'class': 'form-control'}),
        label='نام پروژه',
    )

    groups = forms.ChoiceField(
        choices = add_group(groups_form),
        label='دسته بندی',
    )

    discribtion_show = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا توضیحات پروژه خود را وارد نمایید', 'class': 'form-control'}),
        label='توضیحات'
    )

    budget = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'لطفا بودجه مورد نیاز پروژه را وارد نمایید', 'class': 'form-control'}),
        label='بودجه'
    )

    needed_time = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا زمان موردنیاز پروژه خود را وارد نمایید', 'class': 'form-control'}),
        label='زمان مورد نیاز'
    )

    site = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا آدرس سایت خود را وارد نمایید', 'class': 'form-control'}),
        label='آدرس سایت'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'class': 'form-control'}),
        label='آدرس ایمیل'
    )

    logo = forms.ImageField(
        label='تصویر پروژه',
    )