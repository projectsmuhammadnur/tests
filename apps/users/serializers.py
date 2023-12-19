from apps.users.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "created_at",
            "updated_at"
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        password = validated_data.get('password')
        if password:
            instance.password = make_password(password)

        instance.save()
        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        user = User.objects.create(**validated_data)
        return user


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "created_at",
            "updated_at"
        ]


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username"
