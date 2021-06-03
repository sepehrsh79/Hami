from django import forms
from django.core import validators

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
        label='کلمه ی عبور'
    )

