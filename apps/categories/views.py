from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.categories.models import Categories
from apps.categories.serializers import CategoriesSerializer, CategoriesRetrieveSerializer


class CategoriesListView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]


class CategoriesDetailView(RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesRetrieveSerializer
    permission_classes = [AllowAny]
