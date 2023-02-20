from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountmanager(BaseUserManager):
    def create_user(self, full_name, email, username, password=None):

        if not username or not email:
            raise ValueError('User must have an Username and Email!')

        user = self.model(
            full_name = full_name,
            username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, full_name, email, username, password):
        user = self.create_user(
            full_name = full_name, 
            username = username,
            password = password,
            email = self.normalize_email(email),
            )
        
        user.is_admin = True
        user.is_active = True
        user.is_superadmin = True
        
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    full_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']

    objects = MyAccountmanager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return self.is_superadmin

    def has_module_perms(self, add_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin