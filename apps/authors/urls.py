from django.urls import path
from .views import (AuthorsListView, AuthorsDetailView)

urlpatterns = [
    path('', AuthorsListView.as_view(), name='authors-list'),
    path('<int:pk>/', AuthorsDetailView.as_view(), name='authors-detail'),
]
