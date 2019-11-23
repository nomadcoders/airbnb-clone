from django.db import models
from django.contrib.auth.models import UserManager


class CustomModelManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class CustomUserManager(CustomModelManager, UserManager):
    pass
