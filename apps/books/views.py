import django_filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.books.filters import BooksSearchFilter
from apps.books.models import Books
from apps.books.serializers import BooksSerializer, BooksRetrieveSerializer


class BooksListView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [AllowAny]


class BooksDetailView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksRetrieveSerializer
    permission_classes = [AllowAny]


class BooksSearchView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = BooksSearchFilter
