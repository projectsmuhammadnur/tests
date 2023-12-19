from rest_framework.serializers import ModelSerializer

from apps.books.models import Books
from rest_framework import serializers


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        exclude = [
            "author_id",
            "category_id",
            "created_at",
            'updated_at'
        ]


class BooksRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        exclude = [
            "updated_at"
        ]
