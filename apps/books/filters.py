import django_filters
from .models import Books


class BooksSearchFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    author_id = django_filters.NumberFilter(label='Author ID')
    category_id = django_filters.NumberFilter(label='Category ID')

    class Meta:
        model = Books
        fields = ['title', 'author_id', 'category_id']
