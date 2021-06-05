from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا شماره خود را وارد نمایید', 'class':'form-control'}),
        label='شماره موبایل'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'class':'form-control'}),
        label='کلمه ی عبور'
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_exists_user = User.objects.filter(username=phone).exists()
        if not is_exists_user:
            raise forms.ValidationError('کاربری با مشخصات وارد شده ثبت نام نکرده است')
        return phone


class RegisterForm(forms.Form):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class':'form-control'}),
        label='نام',
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class':'form-control'}),
        label='نام خانوادگی',
    )

    identifier_code = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا کد معرف را وارد نمایید', 'class':'form-control'}),
        label='کد معرف (اختیاری)',
        required=False
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'class':'form-control'}),
        label='کلمه ی عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا تکرار کلمه عبور خود را وارد نمایید', 'class':'form-control'}),
        label='تکرار کلمه ی عبور'
    )

    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا شماره موبایل خود را وارد نمایید', 'class':'form-control'}),
        label='شماره موبایل (نام کاربری)',
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_str = str(phone)
        if len(phone_str) != 11:
            raise forms.ValidationError('تعداد ارقام شماره موبایل باید ۱۱ رقم باشد')
        return phone

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password


class Verify(forms.Form):

    verification_code = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا کد تایید پیامکی  را وارد نمایید', 'class':'form-control'}),
        label='کد پیامکی',
    )