from django.urls import path

from .views import (
    ProjectsList, 
    FilterProjectsView, 
    project_detail, 
    ProjectsListByGroup,
    create_project,
    SearchProjectsView
    )

urlpatterns = [
    path('projects/', ProjectsList.as_view()),
    path('projects/filter', FilterProjectsView.as_view()),
    path('projects/search', SearchProjectsView.as_view()),
    path('projects/<int:projectID>',project_detail),
    path('projects/<slug:group_name>', ProjectsListByGroup.as_view()),
    path('projects/create/', create_project),
]