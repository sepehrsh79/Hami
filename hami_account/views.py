from hami_account.models import UserCustomize ,SubBranches, Branch
from django.http import request
from .forms import LoginForm, RegisterForm, Verify, EditGroups
from hami_supports.models import Support
from hami_projects.models import Group, Project
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from sms import send_sms
import random
from datetime import datetime


def verify_code_generator ():
    n = random.randint(10000,99999)
    return n

def identifier_code_generator ():
    code = random.randint(10000,99999)
    return code

verify_code = verify_code_generator()
generated_icode = identifier_code_generator()
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
    identifier_code = user_informations['identifier_code']

    send_sms(
            f'کد احراز هویت شما:{verify_code}',
            '+989056967179',
            ['+989398477890'],
            fail_silently=False
            )
            
    verify_form = Verify(request.POST or None)
    if verify_form.is_valid():
        verification_code = verify_form.cleaned_data.get('verification_code')
        verification_code = int(verification_code)

        #first check verification of code then create a user with identifier_code
        if verification_code == verify_code:
            user = User.objects.create_user(
                username=user_phone, 
                email='',
                password=user_password, 
                first_name=user_fname, 
                last_name=user_lname
            )   
            UserCustomize.objects.create(user=user,identifier_code=generated_icode)
            Branch.objects.create(head_branch=user, identifier_code=generated_icode)

            #second check if user identifier_code is exists then create a sub brach for him (related to head bracn)
            head_branch = Branch.objects.filter(identifier_code=identifier_code).first()
            if head_branch:
                SubBranches.objects.create(head_branch=head_branch, sub_branche_user=user)
                login(request, user)
                return redirect('/')
            else:
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

def logout_user(request):
    logout(request)
    return redirect('/account/login')


def user_profile(request):
    if not request.user.is_authenticated :
       return redirect("/account/login")
    else:

        context = {
            
        }
        return render(request, 'user_panel.html',context)


def admin_profile(request):
    #check admin verification  
    if not request.user.is_staff:
       return redirect("/account/login")
    else:
        today_date = datetime.now().date()
        all_supports = Support.objects.all()
        today_supports = Support.objects.filter(date__iexact=today_date)
        completed_project = Project.objects.filter(status="disable")
        projects = Project.objects.all()

        context = {
            'today_supports':today_supports.count(),
            'completed_project':completed_project.count(),
            'all_supports':all_supports.count(),
            'projects' : projects
        }
        return render(request, 'panel/admin_panel.html',context)


def create_group (request):
    #check admin verification  
    if not request.user.is_staff:
       return redirect("/account/login")
    else:
        groups = Group.objects.all()
        if request. method == "POST":
            edit_groups = EditGroups(request.POST, request.FILES)
            if edit_groups.is_valid():
                print("hello")
                title = edit_groups.cleaned_data.get('title')
                admin_title = edit_groups.cleaned_data.get('admin_title')
                discribtion = edit_groups.cleaned_data.get('discribtion')
                image = edit_groups.cleaned_data.get('image')

                Group.objects.create(title=title, slug=admin_title, discribtion= discribtion, image=image)
        edit_groups = EditGroups()

        context = {
            'groups': groups,
            'edit_groups':edit_groups
        }


        return render(request, 'panel/create_group.html',context)
        

def users_report(request):
    #check admin verification
    if not request.user.is_staff:
       return redirect("/account/login")
    else:
        totall = 0
        branchs = Branch.objects.all()
        branch = branchs[0]
        #send it to anothet view and for all subbranch in all without first do this function call

        #do it in Branch mdoel from line 205
    context = {
       'branchs' : branchs,
        'totall':totall
    }
    return render(request, 'panel/users_report.html', context)

#
# def users_report(request):
#     #check admin verification
#     if not request.user.is_staff:
#        return redirect("/account/login")
#     else:
#         totall = 0
#         branchs = Branch.objects.all()
#         branch = branchs[0]
#         #send it to anothet view and for all subbranch in all without first do this function call
#         subs = branch.subbranches_set.all()
#         for sub in subs:
#            totall = totall + sub.get_subbranch_sups
#         #do it in Branch mdoel from line 205
#     context = {
#        'branchs' : branchs,
#         'totall':totall
#     }
#     return render(request, 'panel/users_report.html',context)
#
