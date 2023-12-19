from apps.categories.models import Categories
from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = [
            "created_at",
            'updated_at'
        ]


class CategoriesRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = [
            "updated_at"
        ]
