from uuid import uuid4

from django.core.validators import (RegexValidator,
                                    MinValueValidator,
                                    MaxValueValidator)
from django.db import models

from app.utils.model_helpers import PHONE_REGEX


class BaseEvent(models.Model):
    """ Abstract model for reservations and events """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Guest(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=18,
                                    validators=[RegexValidator(PHONE_REGEX)],
                                    blank=True)
    email = models.EmailField(blank=True, unique=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Event(BaseEvent):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Reservation(BaseEvent):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    party_size = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)])
    seating_preference = models.CharField(max_length=50, blank=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.guest.name} - {self.date}'
