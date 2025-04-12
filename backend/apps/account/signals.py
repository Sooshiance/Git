from typing import Any

from django.conf import settings
from django.db.models.signals import post_save

from .models import Profile


def create_profile(
    sender: type,
    instance,
    created: bool,
    **kwargs: Any,
) -> None:
    if created:
        user = instance
        Profile.objects.create(user=user, email=user.email)


post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)
