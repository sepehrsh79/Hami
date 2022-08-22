import jdatetime
from django.contrib.auth.decorators import login_required
from unidecode import unidecode
from django.shortcuts import redirect, render
from .models import Project, Comment, ProjectCategory
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.http import Http404
from .forms import CommentForm, ProjectForm
from datetime import datetime
from supports.forms import SupportForm
from django.db.models import Q



class ProjectsList(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Project.objects.all().order_by('-id').distinct()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['project_categories'] = ProjectCategory.objects.all()
        return context


class FilterProjectsView(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        status = request.GET['status']
        project_category = request.GET['project_category']
        range = int(request.GET['range'])
        price_range = [100000, 500000, 1000000, 5000000, 5000000]
        chosen_projects = []
        if status == 'all' and project_category == 'all':
            projects = Project.objects.all().order_by('-id').distinct()
            if range == 4:
                for project in projects:
                    need = project.budget - project.current_budget
                    if need > price_range[range]:
                        chosen_projects.append(project)
            else:
                for project in projects:
                    need = project.budget - project.current_budget
                    if need <= price_range[range]:
                        chosen_projects.append(project)

            return chosen_projects

        elif status == 'all' and project_category != 'all':
            projects = Project.objects.filter(project_category__slug=project_category).order_by('-id').distinct()
            if range == 4:
                for project in projects:
                    need = project.budget - project.current_budget
                    if need >= price_range[range]:
                        chosen_projects.append(project)
            else:
                for project in projects:
                    need = project.budget - project.current_budget
                    if need <= price_range[range]:
                        chosen_projects.append(project)

            return chosen_projects

        elif status != 'all' and project_category == 'all':
            projects = Project.objects.filter(status=status).order_by('-id').distinct()
            if range == 4:
                for project in projects:
                    need = project.budget - project.current_budget
                    if need >= price_range[range]:
                        chosen_projects.append(project)
            else:
                for project in projects:
                    need = project.budget - project.current_budget
                    if need <= price_range[range]:
                        chosen_projects.append(project)

            return chosen_projects

        elif status != 'all' and project_category != 'all':
            projects = Project.objects.filter(status=status, project_category__slug=project_category)
            if range == 4:
                for project in projects:
                    need = project.budget - project.current_budget
                    if need >= price_range[range]:
                        chosen_projects.append(project)
            else:
                for project in projects:
                    need = project.budget - project.current_budget
                    if need <= price_range[range]:
                        chosen_projects.append(project)

            return chosen_projects

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['project_categories'] = ProjectCategory.objects.all()
        return context


class SearchProjectsView(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Project.objects.filter(
                Q(name_show__icontains=query) | Q(description_show__icontains=query), status='enable')
        raise Http404('پروژه مورد نظر یافت نشد')


def project_detail(request, **kwargs):
    selected_project_id = kwargs['projectID']
    support_form = SupportForm(request.POST or None, initial={'project_id': selected_project_id})
    
    selected_project = Project.objects.get(pk=selected_project_id)
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
        'comments': comments,
        'supports': supports,
        'comments_count': comments.count(),
        'comment_form': comment_form,
        'support_form': support_form
    }
    if 'support' in request.session:
        context['support'] = request.session['support']['status']
        del request.session['support']

    return render(request, 'project_detail.html', context)


class ProjectsListByCategory(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Project.objects.get_by_category_id(category_id)


@login_required(login_url='/account/login')
def create_project(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        if request.method == "POST":
            create_project_form = ProjectForm(request.POST, request.FILES)

            if create_project_form.is_valid():
                name_show = create_project_form.cleaned_data.get('name_show')
                project_category = create_project_form.cleaned_data.get('project_category')
                usr = User.objects.filter(id=user_id).first()
                description_show = create_project_form.cleaned_data.get('description_show')
                budget = create_project_form.cleaned_data.get('budget')
                time = datetime.strptime(unidecode(create_project_form.cleaned_data.get('needed_time')), '%Y/%m/%d').date()
                needed_time = jdatetime.date(time.year, time.month, time.day).togregorian()
                site = create_project_form.cleaned_data.get('site')
                email = create_project_form.cleaned_data.get('email')
                logo = create_project_form.cleaned_data.get('logo')

                project = Project.objects.create(
                    name="پروژه جدید",
                    name_show=name_show, 
                    project_category=project_category,
                    creator=usr,
                    description='',
                    description_show=description_show,
                    budget=budget,
                    current_budget=0,
                    needed_time=needed_time,
                    site=site,
                    email=email,
                    logo=logo, 
                    status="notshow")

                project.save()
                data = {'status': 'ok'}
                request.session['create_project'] = data
                return redirect('/')
        create_project_form = ProjectForm()
        context = {'create_project_form': create_project_form}
        return render(request, 'create_project.html', context)
    else:
        return redirect("/account/login")


@login_required(login_url='/account/login')
def edit_project(request, project_id):
    try:
        instance = Project.objects.get(pk=project_id)
    except User.DoesNotExist:
        return redirect('/account/admin') if request.user.is_staff else redirect('/account/user')

    if request.user.is_staff or instance.creator == request.user:
        if request.method == "POST":
            project_form = ProjectForm(request.POST, request.FILES)
            if project_form.is_valid():
                instance.name_show = project_form.cleaned_data.get('name_show')
                instance.project_category = project_form.cleaned_data.get('project_category')
                instance.description_show = project_form.cleaned_data.get('description_show')
                instance.budget = project_form.cleaned_data.get('budget')
                time = datetime.strptime(unidecode(project_form.cleaned_data.get('needed_time')), '%Y/%m/%d').date()
                instance.needed_time = jdatetime.date(time.year, time.month, time.day).togregorian()
                instance.site = project_form.cleaned_data.get('site')
                instance.email = project_form.cleaned_data.get('email')
                instance.logo = project_form.cleaned_data.get('logo')
                instance.save()
                data = {'status': 'true'}
                request.session['edit_project'] = data
                return redirect('/account/admin') if request.user.is_staff else redirect('/account/user')

        project_form = ProjectForm(initial={
            "name_show": instance.name_show,
            "project_category": instance.project_category,
            "description_show": instance.description_show,
            "budget": instance.budget,
            "needed_time": instance.needed_time,
            "site": instance.site,
            "email": instance.email,
            "logo": instance.logo
        })
        context = {'project_form': project_form, 'instance': instance}
        return render(request, 'panel/edit_project.html', context)
    else:
        return redirect("/account/login")


@login_required(login_url='/account/login')
def remove_project(request, project_id):
    try:
        instance = Project.objects.get(pk=project_id)
    except User.DoesNotExist:
        return redirect('/account/admin') if request.user.is_staff else redirect('/account/user')
    if request.user.is_staff or instance.creator == request.user:
        instance.delete()
        data = {'status': 'true'}
        request.session['remove_project'] = data
        return redirect('/account/admin') if request.user.is_staff else redirect('/account/user')
    else:
        return redirect("/account/login")


@login_required(login_url='/account/login')
def update_project(request, project_id):
    try:
        instance = Project.objects.get(pk=project_id)
    except User.DoesNotExist:
        return redirect('/account/admin') if request.user.is_staff else redirect('/account/user')
    if request.user.is_staff or instance.creator == request.user:
        instance.status = 'enable' if instance.status == 'notshow' else 'notshow'
        instance.save()
        data = {'status': instance.status}
        request.session['update_project'] = data
        return redirect('/account/admin') if request.user.is_staff else redirect('/account/user')
    else:
        return redirect("/account/login")

