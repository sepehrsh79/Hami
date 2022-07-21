from django.shortcuts import render
import itertools
from hami_setting.models import SiteSetting, Slider
from hami_projects.models import ProjectCategory, Project
from hami_supports.models import Support
from django.db.models import Sum


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    project_categories = ProjectCategory.objects.all()

    context = {
        'setting': site_setting,
        'project_categories': project_categories
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    slides = Slider.objects.all()
    project_categories = ProjectCategory.objects.all()
    active_projects = Project.objects.filter(status='enable')
    all_projects = Project.objects.all()

    context = {
        'slides': slides,
        'groups': my_grouper(4, project_categories),
        'projects': active_projects,
        'project_count': all_projects.count(),
        'enb_project_count': active_projects.count(),
    }
    if 'login_user' in request.session:
        context['login_user'] = request.session['login_user']['status']
        del request.session['login_user']

    if 'logout_user' in request.session:
        context['logout_user'] = request.session['logout_user']['status']
        del request.session['logout_user']

    if 'create_project' in request.session:
        context['create_project'] = request.session['create_project']['status']
        del request.session['create_project']

    if 'register_user' in request.session:
        context['register_user'] = request.session['register_user']['status']
        del request.session['register_user']

    all_supports_amount = Support.objects.all()
    if all_supports_amount:
        support_amount = all_supports_amount.aggregate(Sum("amount"))
        supports = support_amount['amount__sum']
    else:
        supports = 0
    context["amount__sum"] = int(supports)

    return render(request, 'home_page.html', context)
