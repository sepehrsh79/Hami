from django.shortcuts import render
import itertools
from hami_setting.models import SiteSetting
from hami_sliders.models import Slider
from hami_projects.models import Group, Project
from hami_sponsors.models import Sponsor



def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Header.html', context)

def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    group = Group.objects.all()

    context = {
        'setting': site_setting,
        'groups' : group
    }
    return render(request, 'shared/Footer.html', context)

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def home_page(request):
    slides = Slider.objects.all()
    group = Group.objects.all()
    active_projects = Project.objects.filter(status='enable')
    all_projects = Project.objects.all()



    context = {
        'slides' : slides,
        'groups' : my_grouper(4, group),
        'projects' : active_projects,
        'project_count' : all_projects.count(),
        'enb_project_count' : active_projects.count(),
    }

    return render(request, 'home_page.html', context)