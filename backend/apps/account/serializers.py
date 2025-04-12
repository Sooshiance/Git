from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as User_Type
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ("username", "password", "email")


# FIXME: Type annotation for parent class
class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User_Type) -> dict[str, Any]:
        token = super().get_token(user)
        token["username"] = user.username
        return token


class ProfileSerializer(serializers.ModelSerializer[Profile]):
    user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = (
            "pid",
            "pk",
            "username",
            "email",
            "user",
        )
        read_only_fields = ("pid", "pk")
