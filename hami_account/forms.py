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
        if len(phone_str) != 10:
            raise forms.ValidationError('تعداد ارقام شماره موبایل باید 10 رقم باشد!')
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password.isdigit() or len(password) < 6 :
            raise forms.ValidationError('کلمه عبور باید بیشتر از 5 کارکتر و شامل حروف و اعداد باشد!')
        return password

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند!')
        return password


class Verify(forms.Form):

    verification_code = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا کد تایید پیامکی  را وارد نمایید', 'class':'form-control'}),
        label='کد پیامکی',
    )


class EditGroups(forms.Form):

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان دسته را وارد نمایید', 'class':'form-control'}),
        label='عنوان دسته'
    )
    admin_title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان مدیریتی دسته را وارد نمایید', 'class':'form-control'}),
        label='عنوان مدیریتی دسته'
    )

    discribtion = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفاتوضیحات را وارد نمایید', 'class':'form-control'}),
        label='توضیحات دسته'
    )

    image = forms.ImageField(
        label='تصویر',
        widget=forms.FileInput(attrs={'class':'form-control btn'})
    )
    
class EditAccount(forms.Form):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class':'form-control'}),
        label='نام'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class':'form-control'}),
        label='نام خانوادگی'
    )

    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا  شماره تماس جدید را وارد نمایید', 'class': 'form-control'}),
        label='شماره تماس جدید',
    )

