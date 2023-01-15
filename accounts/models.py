from django.db import models
from django.contrib.auth.models import AbstractUser
# from .managers import UserManager
from django.contrib.auth.models import UserManager

class User(AbstractUser):
    email = models.EmailField(max_length=225, unique=True)
    phone_num = models.CharField(max_length=11)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name']

    objects = UserManager()

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # @property
    # def is_staff(self):
    #     return self.is_admin



