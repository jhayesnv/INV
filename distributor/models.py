from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models

from app.utils.model_helpers import PHONE_REGEX


class SalesRepresentative(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=18,
                                    validators=[RegexValidator(PHONE_REGEX)],
                                    blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Distributor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=18,
                                    validators=[RegexValidator(PHONE_REGEX)],
                                    blank=True)
    order_dates = models.CharField(max_length=25, blank=True)
    sales_reps = models.ManyToManyField(SalesRepresentative,
                                        blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
