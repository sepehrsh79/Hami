from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.ProjectsList.as_view()),
    path('projects/filter', views.FilterProjectsView.as_view()),
    path('projects/search', views.SearchProjectsView.as_view()),
    path('projects/<int:projectID>', views.project_detail),
    path('projects/category/<int:category_id>', views.ProjectsListByCategory.as_view()),
    path('projects/create/', views.create_project),
    path('projects/<int:project_id>/edit', views.edit_project),
    path('projects/<int:project_id>/remove', views.remove_project),
    path('projects/<int:project_id>/update', views.update_project)
]
