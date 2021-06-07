from django.http import request
from .forms import LoginForm, RegisterForm, Verify
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from sms import send_sms
import random

def verify_code_generator ():
    n = random.randint(10000,99999)
    return n

verify_code = verify_code_generator()

user_info = None

def register_user(request):

    if request.user.is_authenticated:
        return redirect('/')
    context = {}
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        phone = register_form.cleaned_data.get('phone')
        phone = int(phone)
        password = register_form.cleaned_data.get('password')
        password = str(password)
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        identifier_code = register_form.cleaned_data.get('identifier_code')

        global user_info
        def user_info():
            info = {'phone':phone, 
            'password':password, 
            'first_name':first_name, 
            'last_name':last_name, 
            'identifier_code':identifier_code }
            return info

        user = User.objects.filter(username=phone)
        if user.exists():
            messages.info(request, 'متاسفانه قبلا کاربری با این شماره تماس ثبت شده است!')
        else:
            send_sms(
                f'کد احراز هویت شما:{verify_code}',
                '+989056967179',
                ['+989398477890'],
                fail_silently=False
            )
            return redirect('/account/verify')

    context['register_form'] = register_form
    return render(request, 'register.html', context)


def verify_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    user_informations = user_info()
    user_phone = user_informations['phone']
    user_password = user_informations['password']
    user_fname = user_informations['first_name']
    user_lname = user_informations['last_name']
    
    verify_form = Verify(request.POST or None)
    if verify_form.is_valid():
        verification_code = verify_form.cleaned_data.get('verification_code')
        verification_code = int(verification_code)

        if verification_code == verify_code:
            user = User.objects.create_user(
                username=user_phone, 
                email='',
                password=user_password, 
                first_name=user_fname, 
                last_name=user_lname
            )

            login(request, user)
            return redirect('/')

        else:
            messages.success(request, 'کد پیامکی وارد شده صحیح نمی باشد!')

    context = {'verify_form' : verify_form}
    return render(request, 'verify.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        phone = login_form.cleaned_data.get('phone')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('phone', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)

def user_profile(request):
    if not request.user.is_authenticated :
       return redirect("/account/login")
    else:

        context = {
            
        }
        return render(request, 'user_panel.html',context)

def admin_profile(request):
    if not request.user.is_staff:
       return redirect("/account/login")
    else:

        context = {
            
        }
        return render(request, 'admin_panel.html',context)


def logout_user(request):
    logout(request)
    return redirect('/account/login')
