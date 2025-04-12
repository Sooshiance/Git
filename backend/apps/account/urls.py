from django.urls import path

from .views import CustomTokenView, ProfileView, UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("token/", CustomTokenView.as_view(), name="token"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
