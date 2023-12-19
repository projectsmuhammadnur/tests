from django.urls import path
from .views import (CategoriesListView, CategoriesDetailView)

urlpatterns = [
    path('', CategoriesListView.as_view(), name='categories-list'),
    path('<int:pk>/', CategoriesDetailView.as_view(), name='categories-detail'),
]
