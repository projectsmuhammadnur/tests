import django_filters
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.books.filters import BooksSearchFilter
from apps.books.models import Books
from apps.books.serializers import BooksSerializer, BooksRetrieveSerializer
from apps.users.permissions import UserPermission


class BooksListView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [UserPermission]


class BooksDetailView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksRetrieveSerializer
    permission_classes = [UserPermission]


class BooksSearchView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [UserPermission]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = BooksSearchFilter
