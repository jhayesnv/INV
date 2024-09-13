from uuid import uuid4

from django.db import models
from distributor.models import Distributor

from app.utils.model_helpers import (REGION_AREA_CHOICES,
                                     FOOD_ORDER_ITEM_UNIT_CHOICES,
                                     BASE_SPIRIT_CHOICES)


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
    par = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)
    quantity_on_hand = models.DecimalField(max_digits=3, decimal_places=1,
                                           default=0.0)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    product_identifier = models.CharField(max_length=64, blank=True)
    area_categories = models.ManyToManyField(Category)
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
    area = models.CharField(max_length=18,
                            choices=REGION_AREA_CHOICES,
                            default='United States')
    sub_regions = models.ManyToManyField(SubRegion)


class Producer(models.Model):
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
    category = models.CharField(max_length=7,
                                choices=CATEGORY_CHOICES,
                                default='Spirits')
    regions = models.ManyToManyField(Region)

    def __str__(self):
        return self.name


class WineRegion(Region):
    """ A more descriptive region entity for advanced wine studies """
    geography = models.TextField(blank=True,
                                 help_text=("country, area, natural features e.g."  # noqa: W605 E501 also WTF!! Eat shit
                                            " mountains, lakes, rivers,"
                                            " forests where in relation to"
                                            " other regions, etc."))
    grapes_allowed = models.TextField(blank=True,
                                      help_text="Not just the obvious ones")
    viticultural_techniques = models.TextField(blank=True,
                                               help_text=("ripeness at harvest,"  # noqa: W605 E501 also WTF!! Eat shit
                                                          " vine training,"
                                                          " harvest dates,"
                                                          " irrigation, etc."))
    vinification_techniques = models.TextField(blank=True,
                                               help_text="Fermentation,"
                                               " percentages of blends, "
                                               " acidfication/must enrichments"
                                               " ,etc.")
    aging_laws = models.TextField(blank=True,
                                  help_text="Oak, length of time in wood/btl, "
                                            "release dates, etc.")
    offical_regional_classication = models.TextField(blank=True,
                                                     help_text="VdT vs. AOP, "
                                                     "etc.")
    sub_regional_classifications = models.TextField(blank=True,
                                                    help_text="Vineyards, "
                                                    "villages, producers")
    major_producers = models.ManyToManyField(Producer,
                                             help_text="At least 5, "
                                             "what makes them unique, "
                                             "sig cuvees, historical lore")
    vintage_knowledge = models.TextField(blank=True,
                                         help_text="Poor/Fair/Good/Excellent "
                                         "- why")
    law_terminology = models.TextField(blank=True,
                                       help_text="Gran Reserva vs. Crianza, "
                                       "etc.")
    specific_terminology = models.TextField(blank=True,
                                            help_text="Aszu Essencia, "
                                            "Hanepoot, Sforzato, etc.")


class WineOrderItem(BaseInventoryItem):
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
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    vintage = models.CharField(max_length=4, blank=True)
    region = models.ForeignKey(WineRegion,
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
    style = models.CharField(max_length=9,
                             choices=STYLE_CHOICES,
                             default='Red')


class SpiritOrderItem(BaseInventoryItem):
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
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)


class BeerOrderItem(BaseInventoryItem):
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
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
