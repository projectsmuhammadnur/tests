from django.urls import path
from .views import (BooksListView, BooksDetailView, BooksSearchView, )

urlpatterns = [
    path('', BooksListView.as_view(), name='books-list'),
    path('<int:pk>/', BooksDetailView.as_view(), name='books-detail'),
    path('search/', BooksSearchView.as_view(), name='books-search'),
]
