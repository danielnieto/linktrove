from django.db import models
from django.utils import timezone


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.utils.translation import gettext_lazy as _
from linktrove.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False,
    )
    first_name = models.CharField(
        _("first name"),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        _("last name"),
        max_length=150,
        blank=True,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into " "this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be "
            "treated as active. Unselect this instead "
            "of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_used_tags(self):
        """Returns all tags used by this user on their links"""
        from taggit.models import Tag

        return Tag.objects.filter(
            links_taggedlink_items__content_object__user=self
        ).distinct()
