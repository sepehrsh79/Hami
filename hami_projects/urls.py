from django.urls import path

from .views import ProductsList, FilterProductsView

urlpatterns = [
    path('projects/', ProductsList.as_view()),
    path('projects/filter', FilterProductsView.as_view()),
]