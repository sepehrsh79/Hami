import jdatetime
import random

from django.db.models import Sum
from unidecode import unidecode
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from sms import send_sms
from hami_projects.models import ProjectCategory, Project
from hami_supports.models import Support
from .forms import LoginForm, RegisterForm, Verify, EditProjectCategory, EditAccount, ChangePass


def code_generator():
    code = random.randint(10000, 99999)
    return code


def sending_sms(code, phone):
    send_sms(
        f'کد احراز هویت شما:{code}',
        '+989056967179',
        [f'+98{phone}'],
    )
    return code


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        phone = int(register_form.cleaned_data.get('phone'))
        password = str(register_form.cleaned_data.get('password'))
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')

        user = User.objects.filter(username=phone)
        register_form = RegisterForm()

        if user.exists():
            messages.info(request, 'متاسفانه قبلا کاربری با این شماره تماس ثبت شده است!')
        else:
            code = code_generator()
            verify_code = sending_sms(code, phone)

            data = {'phone': phone, 'password': password, 'first_name': first_name, 'last_name': last_name, 'verify_code': verify_code,
                    'create_date': str(datetime.now())}
            request.session['user_info'] = data
            return redirect('/account/verify')

    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)


def verify_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    user_info = request.session['user_info']
    user_phone = user_info['phone']
    user_password = user_info['password']
    user_fname = user_info['first_name']
    user_lname = user_info['last_name']
    verify_code = user_info['verify_code']
    verify_code_create_date = user_info['create_date']

    if 'verify' in request.POST:
        code = code_generator()
        verify_code = sending_sms(code, user_phone)
        request.session['user_info']['verify_code'] = verify_code

    verify_form = Verify(request.POST or None)
    if request.POST and 'verify' not in request.POST:
        if verify_form.is_valid():
            verification_code = verify_form.cleaned_data.get('verification_code')
            verification_code = int(verification_code)
            now = datetime.now()
            if verification_code == verify_code and \
                    now - datetime.strptime(verify_code_create_date, "%Y-%m-%d %H:%M:%S.%f") < timedelta(minutes=10):
                user = User.objects.create_user(
                    username=user_phone,
                    email='',
                    password=user_password,
                    first_name=user_fname,
                    last_name=user_lname
                )

                del request.session['user_info']
                login(request, user)
                data = {'status': 'ok'}
                request.session['register_user'] = data
                return redirect('/')
            else:
                messages.success(request, 'کد پیامکی وارد شده صحیح نمی باشد!')
    else:
        verify_form = Verify(request.POST or None)

    context = {'verify_form': verify_form}
    return render(request, 'verify.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {}
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        phone = login_form.cleaned_data.get('phone')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=phone, password=password)
        if user is not None:
            login(request, user)
            data = {'status': 'ok'}
            request.session['login_user'] = data
            return redirect('/')
        else:
            login_form.add_error('phone', 'کاربری با مشخصات وارد شده یافت نشد')

    context['login_form'] = login_form
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    data = {'status': 'ok'}
    request.session['logout_user'] = data
    return redirect('/')


@login_required(login_url='/account/login')
def edit_account(request):
    username = request.user.username
    user = User.objects.get(username=username)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')
    edit_form = EditAccount(request.POST or None, initial={'first_name': user.first_name, 'last_name': user.last_name,
                                                           'phone': user.username})
    if edit_form.is_valid():
        first_name = edit_form.cleaned_data.get('first_name')
        last_name = edit_form.cleaned_data.get('last_name')
        phone = edit_form.cleaned_data.get('phone')

        user.first_name = first_name
        user.last_name = last_name
        user.username = int(phone)
        user.save()
        return redirect('/account/admin') if user.is_staff else redirect('/account/user')

    context = {'edit_form': edit_form}
    return render(request, 'edit_account.html', context)


def change_password(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        user_username = request.user.username
        user = User.objects.filter(username=user_username).first()
        if user:
            change_pass_form = ChangePass(request.POST, None)
            if change_pass_form.is_valid():
                password = change_pass_form.cleaned_data.get('password')
                user.set_password(f'{password}')
                user.save()
        else:
            redirect('/account/register')
    context = {
        'change_pass': ChangePass,
    }
    return render(request, 'change_password.html', context)


@login_required
def user_profile(request):
    if not request.user.is_authenticated:
        return redirect("/account/login")
    else:
        if request.user.is_staff:
            return redirect("/account/admin")
        username = request.user.username
        user = User.objects.filter(username=username).first()

        user_supports = Support.objects.filter(supporter=user)
        user_projects = Project.objects.filter(creator=user)
        context = {
            'user_projects': user_projects,
            'user_supports': user_supports,
            'user_supports_count': user_supports.count(),
            'user_projects_count': user_projects.count()
        }
        if 'remove_project' in request.session:
            context['remove_project'] = request.session['remove_project']['status']
            del request.session['remove_project']
        if 'edit_project' in request.session:
            context['edit_project'] = request.session['edit_project']['status']
            del request.session['edit_project']

        return render(request, 'panel/user_panel.html', context)


@login_required
def admin_profile(request):
    # check admin verification
    if not request.user.is_staff:
        return redirect("/account/login")
    else:
        today_date = datetime.now().date()
        all_supports = Support.objects.all().aggregate(Sum('amount'))['amount__sum']
        today_supports = Support.objects.filter(date__iexact=today_date).aggregate(Sum('amount'))['amount__sum']
        completed_project = Project.objects.filter(status="disable")
        projects = Project.objects.all()

        context = {
            'today_supports': today_supports if all_supports else 0,
            'completed_project': completed_project.count(),
            'all_supports': all_supports if all_supports else 0,
            'projects': projects
        }
        if 'remove_project' in request.session:
            context['remove_project'] = request.session['remove_project']['status']
            del request.session['remove_project']
        if 'update_project' in request.session:
            context['update_project'] = request.session['update_project']['status']
            del request.session['update_project']
        if 'edit_project' in request.session:
            context['edit_project'] = request.session['edit_project']['status']
            del request.session['edit_project']

        return render(request, 'panel/admin_panel.html', context)


@login_required
def create_edit_category(request, category_id=None):
    # check admin verification
    if not request.user.is_staff:
        return redirect("/account/login")
    else:
        instance = None
        if category_id:
            categories = ProjectCategory.objects.filter(id=category_id)
            if categories.exists():
                instance = categories.first()
        if request.method == "POST":
            if instance:
                edit_category = EditProjectCategory(request.POST, request.FILES, initial={
                    'title': instance.title, 'slug': instance.slug,
                    'description': instance.description, 'image': instance.image
                })
                if edit_category.is_valid():
                    instance.title = edit_category.cleaned_data.get('title')
                    instance.slug = edit_category.cleaned_data.get('slug')
                    instance.description = edit_category.cleaned_data.get('description')
                    instance.image = edit_category.cleaned_data.get('image')
                    instance.save()
                    data = {'status': 'ok'}
                    request.session['edit_category'] = data
            else:
                edit_category = EditProjectCategory(request.POST, request.FILES)
                if edit_category.is_valid():
                    title = edit_category.cleaned_data.get('title')
                    admin_title = edit_category.cleaned_data.get('slug')
                    description = edit_category.cleaned_data.get('description')
                    image = edit_category.cleaned_data.get('image')
                    ProjectCategory.objects.create(title=title, slug=admin_title, description=description, image=image)
                    data = {'status': 'ok'}
                    request.session['create_category'] = data
        else:
            edit_category = EditProjectCategory(
                initial={'title': instance.title, 'slug': instance.slug,
                         'description': instance.description, 'image': instance.image}) if instance \
                else EditProjectCategory()

        project_categories = ProjectCategory.objects.all()
        context = {
            'project_categories': project_categories,
            'edit_category': edit_category,
            'title': 'افزودن' if not instance else 'ویرایش'
        }

        if 'edit_category' in request.session:
            context['edit_category'] = request.session['edit_category']['status']
            del request.session['edit_category']
        if 'create_category' in request.session:
            context['create_category'] = request.session['create_category']['status']
            del request.session['create_category']   
        if 'remove_category' in request.session:
            context['remove_category'] = request.session['remove_category']['status']
            del request.session['remove_category']

        return render(request, 'panel/create_group.html', context)


@login_required
def remove_category(request, category_id):
    if not request.user.is_staff:
        return redirect("/account/login")
    try:
        ProjectCategory.objects.get(id=category_id).delete()
    except ProjectCategory.DoesNotExist:
        return redirect('/account/admin/manage-category')
    data = {'status': 'ok'}
    request.session['remove_category'] = data
    return redirect('/account/admin/manage-category')


@login_required
def manage_users(request):
    # check admin verification
    if not request.user.is_staff:
        return redirect("/account/login")

    all_users = User.objects.all()

    context = {
        'all_users': all_users,
    }
    if 'change_user_role' in request.session:
        context['change_user_role'] = request.session['change_user_role']['status']
        del request.session['change_user_role']
    return render(request, 'panel/manage_users.html', context)


@login_required
def manage_supports(request):
    # check admin verification
    if not request.user.is_staff:
        return redirect("/account/login")
    _date_from = ''
    _date_to = ''
    supports = Support.objects.all().order_by('date')

    if request.POST:
        _date_from = request.POST.get('date-from', None)
        _date_to = request.POST.get('date-to', None)
        if _date_from and _date_to:
            jalali_date_from = datetime.strptime(unidecode(_date_from), '%Y/%m/%d').date()
            jalali_date_to = datetime.strptime(unidecode(_date_to), "%Y/%m/%d").date()
            date_from = jdatetime.date(jalali_date_from.year, jalali_date_from.month, jalali_date_from.day).togregorian()
            date_to = jdatetime.date(jalali_date_to.year, jalali_date_to.month, jalali_date_to.day).togregorian()
            supports = Support.objects.filter(date__gte=date_from, date__lte=date_to).order_by('date')
        elif _date_from and not _date_to:
            jalali_date_from = datetime.strptime(unidecode(_date_from), '%Y/%m/%d').date()
            date_from = jdatetime.date(jalali_date_from.year, jalali_date_from.month, jalali_date_from.day).togregorian()
            supports = Support.objects.filter(date__gte=date_from).order_by('date')
        elif not _date_from and _date_to:
            jalali_date_to = datetime.strptime(unidecode(_date_to), "%Y/%m/%d").date()
            date_to = jdatetime.date(jalali_date_to.year, jalali_date_to.month, jalali_date_to.day).togregorian()
            supports = Support.objects.filter(date__lte=date_to).order_by('date')
        else:
            supports = Support.objects.all().order_by('date')

    context = {
        'supports': supports,
        'date_from': _date_from,
        'date_to': _date_to
    }
    return render(request, 'panel/manage-supports.html', context)


@login_required
def change_user_role(request, user_id):
    if not request.user.is_staff:
        return redirect("/account/login")
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return redirect('/account/admin/manage-users')
    user.is_staff = not user.is_staff
    user.save()
    data = {'status': 'true'}
    request.session['change_user_role'] = data
    return redirect('/account/admin/manage-users')


@login_required
def remove_user(request, user_id):
    if not request.user.is_staff:
        return redirect("/account/login")
    try:
        User.objects.get(pk=user_id).delete()
    except User.DoesNotExist:
        return redirect('/account/admin/manage-users')
    data = {'status': 'true'}
    request.session['remove_user'] = data
    return redirect('/account/admin/manage-users')
