from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Project, Comment, Group
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.http import Http404
from .forms import CommentForm, CreateProject
from datetime import datetime
from hami_supports.forms import SupportForm


class ProjectsList(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self):
        lookup = (Q(status='enable') | Q(status='disable'))
        return Project.objects.filter(lookup).order_by('-id').distinct()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['groups'] = Group.objects.all()
        return context

class FilterProjectsView(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        status = request.GET['status']
        group = request.GET['group']
        range = int(request.GET['range'])
        price_range = [100000, 500000, 1000000, 5000000, 5000000]
        chosen_projects = []
        if status == 'all' and group == 'all':
            lookup = (Q(status='enable') | Q(status='disable'))
            projects = Project.objects.filter(lookup).order_by('-id').distinct()
            if range == 4:
                for project in projects:
                    need = project.budget - project.Currentـbudget
                    if need > price_range[range]:
                        chosen_projects.append(project)
            else:
                for project in projects:
                    need = project.budget - project.Currentـbudget
                    if need <= price_range[range]:
                        chosen_projects.append(project)

            return chosen_projects

        elif status == 'all' and group != 'all':
            lookup = (Q(status='enable') | Q(status='disable'))
            projects = Project.objects.filter(lookup, Groups__slug=group).order_by('-id').distinct()
            if range == 4:
                for project in projects:
                    need = project.budget - project.Currentـbudget
                    if need >= price_range[range]:
                        chosen_projects.append(project)
            else:
                for project in projects:
                    need = project.budget - project.Currentـbudget
                    if need <= price_range[range]:
                        chosen_projects.append(project)

            return chosen_projects

        elif status != 'all' and group == 'all':
            projects = Project.objects.filter(status=status).order_by('-id').distinct()
            if range == 4:
                for project in projects:
                    need = project.budget - project.Currentـbudget
                    if need >= price_range[range]:
                        chosen_projects.append(project)
            else:
                for project in projects:
                    need = project.budget - project.Currentـbudget
                    if need <= price_range[range]:
                        chosen_projects.append(project)

            return chosen_projects

        elif status != 'all' and group != 'all':
            projects = Project.objects.filter(status=status, Groups__slug=group)
            if range == 4:
                for project in projects:
                    need = project.budget - project.Currentـbudget
                    if need >= price_range[range]:
                        chosen_projects.append(project)
            else:
                for project in projects:
                    need = project.budget - project.Currentـbudget
                    if need <= price_range[range]:
                        chosen_projects.append(project)

            return chosen_projects


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['groups'] = Group.objects.all()
        return context


class SearchProjectsView(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Project.objects.search(query)
        raise Http404('صفحه ی مورد نظر یافت نشد')


def project_detail(request, **kwargs):
    selected_project_id = kwargs['projectID']
    support_form = SupportForm(request.POST or None, initial={'project_id':selected_project_id})
    
    selected_project = Project.objects.get_by_id(selected_project_id)
    if selected_project is None:
        raise Http404('پروژه مورد نظر یافت نشد')

    
    comments = selected_project.comment_set.filter(status='enable')
    supports = selected_project.support_set.order_by('-date').all() #sort by date

    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        name = comment_form.cleaned_data.get('name')
        subject = comment_form.cleaned_data.get('subject')
        message = comment_form.cleaned_data.get('message')
        dateN = datetime.now()
        
        Comment.objects.create(name=name, subject=subject, message=message, date=dateN, project=selected_project)
    comment_form = CommentForm()

    context = {
        'project': selected_project,
        'comments' : comments,
        'supports' : supports,
        'comments_count' : comments.count(),
        'comment_form' : comment_form,
        'support_form' : support_form
        
    }

    return render(request, 'project_detail.html', context)


class ProjectsListByGroup(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self):
        group_name = self.kwargs['group_name']
        return Project.objects.get_by_groups(group_name)


def create_project(request):

    if request.user.is_authenticated:
        user_id = request.user.id
        if request.method == "POST":
            create_project_form = CreateProject(request.POST, request.FILES)

            if create_project_form.is_valid():
                name_show = create_project_form.cleaned_data.get('name_show')
                gr = create_project_form.cleaned_data.get('groups')
                group = Group.objects.filter(slug=gr).first()
                usr = User.objects.filter(id=user_id).first()
                discribtion_show = create_project_form.cleaned_data.get('discribtion_show')
                budget = create_project_form.cleaned_data.get('budget')
                needed_time = create_project_form.cleaned_data.get('needed_time')
                site = create_project_form.cleaned_data.get('site')
                email = create_project_form.cleaned_data.get('email')
                logo = create_project_form.cleaned_data.get('logo')

                project = Project.objects.create(
                    name="پروژه جدید" , 
                    name_show=name_show, 
                    Groups=group , 
                    creator= usr ,
                    discribtion='' ,
                    discribtion_show=discribtion_show , 
                    order=0 ,
                    budget=budget , 
                    Currentـbudget=0 , 
                    needed_time=needed_time , 
                    site=site , 
                    email=email , 
                    logo=logo, 
                    status="notshow")

                project.save()
                data = {'status': 'ok'}
                request.session['create_project'] = data
                return redirect('/')
        create_project_form = CreateProject()
        context = {
        'create_project_form': create_project_form
    }
        return render(request, 'create_project.html', context)
    else:
        return redirect("/account/login")