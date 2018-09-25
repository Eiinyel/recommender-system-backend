from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from recommender import choices


class CustomUserManager(BaseUserManager):
    def create(self, email, password, **extra_fields):
        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('You should include an email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('accepted_terms', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super users must have is_staff flag activated')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super users must have is_superuser flag activated')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    first_name = models.CharField(null=True, blank=True, max_length=140, verbose_name=_('First name'))
    last_name = models.CharField(null=True, blank=True, max_length=140, verbose_name=_('Last name'))
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    birth_date = models.DateField(null=True, blank=True, verbose_name=('Birth date'))
    accepted_terms = models.BooleanField(default=True, verbose_name=_('Accepted terms'))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


class Item(models.Model):

    name = models.CharField(blank=True, max_length=140, verbose_name=_('Name'))
    description = models.TextField(blank=True, max_length=140, verbose_name=_('Description'))
    country = models.CharField(blank=True, max_length=140, verbose_name=_('Country'))
    city = models.CharField(blank=True, max_length=140, verbose_name=_('City'))

    def __str__(self):
        return str(self.id)
