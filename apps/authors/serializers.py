from apps.authors.models import Authors
from rest_framework import serializers


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        exclude = [
            "created_at",
            'updated_at'
        ]


class AuthorsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        exclude = [
            "updated_at"
        ]
