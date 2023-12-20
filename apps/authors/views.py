from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.authors.models import Authors
from apps.authors.serializers import AuthorsSerializer, AuthorsRetrieveSerializer


class AuthorsListView(ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [AllowAny]


class AuthorsDetailView(RetrieveAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsRetrieveSerializer
    permission_classes = [AllowAny]
