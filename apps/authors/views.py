from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.authors.models import Authors
from apps.authors.serializers import AuthorsSerializer, AuthorsRetrieveSerializer
from apps.users.permissions import UserPermission


class AuthorsListView(ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [UserPermission]


class AuthorsDetailView(RetrieveAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsRetrieveSerializer
    permission_classes = [UserPermission]
