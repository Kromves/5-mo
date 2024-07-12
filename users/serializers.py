from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Code
from random import randint
from django.utils import timezone

class RegistrationValidationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise serializers.ValidationError("Username already exists")

class CodeValidationSerializer(serializers.Serializer):
    code = serializers.IntegerField(min_value=100000, max_value=999999)

class UserAuthenticationValidationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()