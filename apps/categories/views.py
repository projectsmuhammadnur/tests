from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.categories.models import Categories
from apps.categories.serializers import CategoriesSerializer, CategoriesRetrieveSerializer
from apps.users.permissions import UserPermission


class CategoriesListView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [UserPermission]


class CategoriesDetailView(RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesRetrieveSerializer
    permission_classes = [UserPermission]
