from .forms import LoginForm, RegisterForm, Verify
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages



user_phone = None

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

        global user_phone
        def user_phone():
            return phone

        user = User.objects.filter(username=phone)
        if not user.exists():
            User.objects.create_user(username=phone, email='', password=password, first_name=first_name, last_name=last_name)
            return redirect('/account/verify')
        else:
            messages.info(request, 'متاسفانه قبلا کاربری با این شاره تماس ثبت شده است!')

    context['register_form'] = register_form
    return render(request, 'register.html', context)


def verify_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    counter = 0
    user_phone_num = user_phone()
    user = User.objects.filter(username=user_phone_num).first()

    verify_form = Verify(request.POST or None)

    if verify_form.is_valid():
        verification_code = verify_form.cleaned_data.get('verification_code')
        
        while counter<3:
            if verification_code == 12345:
                login(request, user)
                counter += 1
                return redirect('/')
            else:
                messages.success(request, 'کد پیامکی وارد شده صحیح نمی باشد!')
        user.delete()

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

def user_profile():
    pass

def logout_user(request):
    logout(request)
    return redirect('/account/login')
