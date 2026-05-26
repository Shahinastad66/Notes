from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        field = ["username", "email", "password"]

        def create(self, validate_date):
            user = User.objects.create_user(**validate_date)
            return User