from django import forms
from .models import ProjectCategory


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

    project_category = forms.ModelChoiceField(
        queryset=ProjectCategory.objects.all(),
        label='دسته بندی',
    )

    description_show = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا توضیحات پروژه خود را وارد نمایید', 'class': 'form-control'}),
        label='توضیحات'
    )

    budget = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'لطفا بودجه مورد نیاز پروژه را وارد نمایید', 'class': 'form-control'}),
        label='بودجه'
    )

    needed_time = forms.CharField(
        widget=forms.TextInput(attrs={'type':'date', 'placeholder': 'لطفا زمان موردنیاز پروژه خود را وارد نمایید', 'class': 'form-control'}),
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
