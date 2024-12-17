from uuid import uuid4

from django.db import models
from distributor.models import Distributor

from app.utils.model_helpers import (REGION_AREA_CHOICES,
                                     FOOD_ORDER_ITEM_UNIT_CHOICES,
                                     BASE_SPIRIT_CHOICES,
                                     BEER_STYLE_AREA_CHOICES)


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


class Update(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    submitted = models.DateTimeField(auto_now_add=True)

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
    par = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)
    quantity_on_hand = models.DecimalField(max_digits=3, decimal_places=1,
                                           default=0.0)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    product_identifier = models.CharField(max_length=64, blank=True)
    needs_ordering = models.BooleanField(default=False)
    latest_price = models.DecimalField(max_digits=5,
                                       decimal_places=2,
                                       default=0.0)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class FoodOrderItem(BaseInventoryItem):
    area_categories = models.ManyToManyField(Category)
    unit = models.CharField(max_length=9,
                            choices=FOOD_ORDER_ITEM_UNIT_CHOICES,
                            default='cs')


class SupplyItem(BaseInventoryItem):
    """ All non-food related restaurant items """
    unit = models.CharField(max_length=9,
                            choices=FOOD_ORDER_ITEM_UNIT_CHOICES,
                            default='cs')


class BaseRegion(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SubRegion(BaseRegion):
    pass


class Region(BaseRegion):
    """ Regions outside of the wine category """
    area = models.CharField(max_length=18,
                            choices=REGION_AREA_CHOICES,
                            default='United States')
    sub_regions = models.ManyToManyField(SubRegion, blank=True)


class Producer(models.Model):
    """ Wine, Beer, Spirit, and Sake producers """
    CATEGORY_CHOICES = [
        ('Wine', 'Wine'),
        ('Beer', 'Beer'),
        ('Spirits', 'Spirits'),
        ('Sake', 'Sake'),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=7,
                                choices=CATEGORY_CHOICES,
                                default='Spirits')
    year_established = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return self.name


class Grape(models.Model):
    """ Wine grapes """
    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('White', 'White'),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=5,
                             choices=COLOR_CHOICES,
                             default='Red')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class WineOrderItem(BaseInventoryItem):
    """ All Wine related entities """
    UNIT_CHOICES = (
        ('cs', 'cs'),
        ('btl', 'btl'),
        ('can', 'can'),
    )
    STYLE_CHOICES = [
        ('Red', 'Red'),
        ('White', 'White'),
        ('Rose', 'Rose'),
        ('Sparkling', 'Sparkling'),
        ('Dessert', 'Dessert'),
    ]
    unit = models.CharField(max_length=9,
                            choices=UNIT_CHOICES,
                            default='cs')
    vintage = models.CharField(max_length=4, blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    grapes = models.ManyToManyField(Grape)
    region = models.ForeignKey(Region,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    sub_region = models.ForeignKey(SubRegion,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)
    style = models.CharField(max_length=9,
                             choices=STYLE_CHOICES,
                             default='Red')
    menu_price = models.DecimalField(max_digits=5, decimal_places=2,
                                     default=10.0)
    is_active = models.BooleanField(default=False)
    is_glass_pour = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)


class SpiritOrderItem(BaseInventoryItem):
    """ All Spirit related entities """
    UNIT_CHOICES = (
        ('cs', 'cs'),
        ('btl', 'btl'),
    )
    unit = models.CharField(max_length=9,
                            choices=UNIT_CHOICES,
                            default='btl')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    category = models.CharField(max_length=7,
                                choices=BASE_SPIRIT_CHOICES,
                                default='Bourbon')
    region = models.ForeignKey(Region,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    sub_region = models.ForeignKey(SubRegion,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)
    menu_price = models.DecimalField(max_digits=5, decimal_places=2,
                                     default=10.0)
    is_well = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    is_one_ounce_pour = models.BooleanField(default=False)


class BeerStyleCategory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Beer style categories'

    def __str__(self):
        return self.name


class BeerStyle(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category = models.ForeignKey(BeerStyleCategory, on_delete=models.CASCADE)
    area = models.CharField(max_length=30,
                            choices=BEER_STYLE_AREA_CHOICES,
                            default='Other')

    def __str__(self):
        return self.name


class BeerOrderItem(BaseInventoryItem):
    """ All Beer related entities """
    UNIT_CHOICES = [
        ('keg', 'keg'),
        ('cans', 'cans'),
        ('btls', 'btls'),
    ]
    FORMAT_CHOICES = [
        ('Draft', 'Draft'),
        ('Can/Btl', 'Can/Btl')
    ]
    unit = models.CharField(max_length=9,
                            choices=UNIT_CHOICES,
                            default='keg')
    format = models.CharField(max_length=7,
                              choices=FORMAT_CHOICES,
                              default='Draft')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    region = models.ForeignKey(Region,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    sub_region = models.ForeignKey(SubRegion,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)
    style = models.ForeignKey(BeerStyle, on_delete=models.CASCADE)
    menu_price = models.DecimalField(max_digits=5, decimal_places=2,
                                     default=10.0)
    is_active = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    is_on_deck = models.BooleanField(default=False)
