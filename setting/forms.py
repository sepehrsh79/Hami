from django import forms


class SiteSettingForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان را وارد نمایید', 'class': 'form-control'}),
        label='عنوان', required=False
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا آدرس را وارد نمایید', 'class': 'form-control'}),
        label='آدرس', required=False
    )

    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'لطفا  شماره تماس را وارد نمایید', 'class': 'form-control'}),
        label='شماره تماس', required=False
    )

    mobile = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'لطفا شماره موبایل را وارد نمایید', 'class': 'form-control'}),
        label='شماره موبایل', required=False
    )

    fax = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'لطفا فکس را وارد نمایید', 'class': 'form-control'}),
        label='فکس', required=False
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا ایمیل را وارد نمایید', 'class': 'form-control'}),
        label='ایمیل', required=False
    )
    
    about_us = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا درباره ما را وارد نمایید', 'class': 'form-control'}),
        label='درباره ما', required=False
    )

    copy_right = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا متن کپی رایت را وارد نمایید', 'class': 'form-control'}),
        label='متن کپی رایت', required=False
    )

    logo_image = forms.ImageField(
        widget=forms.FileInput(attrs={'placeholder': 'لطفا لوگو سایت را وارد نمایید', 'class': 'form-control'}),
        label='لوگو سایت', required=False
    )


class SiteSliderForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان را وارد نمایید', 'class': 'form-control'}),
        label='عنوان'
    )

    image = forms.ImageField(
        widget=forms.FileInput(attrs={'placeholder': 'لطفا تصویر را وارد نمایید', 'class': 'form-control'}),
        label='تصویر',
    )
