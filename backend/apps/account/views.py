from typing import Any

from core.response import error_response, success_response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Profile
from .serializers import CustomTokenSerializer, ProfileSerializer, UserSerializer

User = get_user_model()


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        super().create(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data["password"]
            serializer.validated_data["password"] = make_password(password)
            self.perform_create(serializer)
            return success_response(data=serializer.data, status_code=201)
        return error_response(error=serializer.errors)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        user = self.get_object()
        try:
            profile = Profile.objects.get(user)
            return profile
        except User.DoesNotExist as ex:
            return str(ex)
