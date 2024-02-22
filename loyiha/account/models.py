from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kw):
        if not email:
            raise TypeError('email xato')
        user = self.model(email=email, **kw)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **kw):
        if not password:
            raise TypeError('parol xato')
        user = self.create_user(email, password, **kw)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, db_index=True)
    name = models.CharField(max_length=221, null=True)
    img = models.ImageField(upload_to='media/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    date_login = models.DateTimeField(auto_now=True, verbose_name='Login time')
    date_created = models.DateTimeField(auto_now=True, verbose_name='Created date')

    objects = AccountManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.name:
            return f'{self.name}'
        return f'{self.email}'