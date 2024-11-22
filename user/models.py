from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from app.utils.model_helpers import PHONE_REGEX


class Position(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    ROLE_CHOICES = (
        ('BOH', 'BOH'),
        ('FOH', 'FOH')
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    phone_number = models.CharField(max_length=18,
                                    validators=[RegexValidator(PHONE_REGEX)],
                                    blank=True)
    hire_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    mast_permit = models.FileField(upload_to='user_docs/employee/',
                                   blank=True)
    food_permit = models.FileField(upload_to='user_docs/employee/',
                                   blank=True)
    role = models.CharField(max_length=3,
                            choices=ROLE_CHOICES,
                            default='FOH')
    positions = models.ManyToManyField(Position, blank=True)

    REQUIRED_FIELDS = ['email']
