from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectsList.as_view()),
    path('filter', views.FilterProjectsView.as_view()),
    path('search', views.SearchProjectsView.as_view()),
    path('<int:projectID>', views.project_detail),
    path('category/<int:category_id>', views.ProjectsListByCategory.as_view()),
    path('create/', views.create_project),
    path('<int:project_id>/edit', views.edit_project),
    path('<int:project_id>/remove', views.remove_project),
    path('<int:project_id>/update', views.update_project)
]
