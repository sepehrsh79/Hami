from django.shortcuts import render
from .models import Project
from django.views.generic import ListView


class ProductsList(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Project.objects.filter(status='enable')


class FilterProductsView(ListView):
    template_name = 'projects_list.html'
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        request = self.request
        answer = request.GET['sort']


        if answer is not None:
            if answer == 'all':
                return Project.objects.all()
            else:
                return Project.objects.filter(status=answer)
            

