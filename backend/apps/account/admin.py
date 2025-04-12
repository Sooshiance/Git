from django.contrib import admin

from .models import Profile


class AdminProfile(admin.ModelAdmin):
    list_display = ["user__username"]


admin.site.register(Profile, AdminProfile)
