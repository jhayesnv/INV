from uuid import uuid4

from django.db import models
from distributor.models import Distributor


class Category(models.Model):
    """ Inventory item categories """
    AREA_CHOICES = (
        ('Kitchen', 'Kitchen'),
        ('Bar', 'Bar'),
        ('Other', 'Other'),
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=7,
                            choices=AREA_CHOICES,
                            default='Kitchen')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class BaseInventoryItem(models.Model):
    """ Abstract model for inventory items """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    par = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    quantity_on_hand = models.DecimalField(max_digits=3, decimal_places=1,
                                           default=0.0)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    product_identifier = models.CharField(max_length=64, blank=True)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class FoodOrderItem(BaseInventoryItem):
    UNIT_CHOICES = (
        ('cs', 'cs'),
        ('box', 'box'),
        ('can', 'can'),
        ('bucket', 'bucket'),
        ('ea', 'ea'),
        ('flats', 'flats'),
        ('sticks', 'sticks'),
        ('#', '#'),
        ('lbs', 'lbs'),
        ('gal', 'gal'),
        ('oz', 'oz'),
        ('dz', 'dz'),
        ('as needed', 'as needed')
    )
    unit = models.CharField(max_length=9,
                            choices=UNIT_CHOICES,
                            default='cs')
    latest_price = models.DecimalField(max_digits=5,
                                       decimal_places=2,
                                       default=0.0)
    last_updated_at = models.DateTimeField(auto_now=True)
