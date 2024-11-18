from uuid import uuid4

from django.db import models

import inventory.models as im
from app.utils.model_helpers import (COCKTAIL_CATEGORY_CHOICES,
                                     BASE_SPIRIT_CHOICES)


class BaseRecipe(models.Model):
    """ Abstract model for bar and kitchen recipes """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class KitchenRecipe(BaseRecipe):
    """ Recipes relating to the kitchen """
    ingredients = models.ManyToManyField(im.FoodOrderItem, blank=True)
    is_gluten_free = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)


class MenuItemRecipe(BaseRecipe):
    """ Aggregate recipes for menu items """
    recipes = models.ManyToManyField(KitchenRecipe, blank=True)
    is_brunch = models.BooleanField(default=False)
    is_social_hour = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)


class BarRecipe(BaseRecipe):
    """ Recipes relating to the bar """
    ingredients = models.ManyToManyField(im.FoodOrderItem, blank=True)


class CocktailRecipe(BaseRecipe):
    """ Recipes relating to cocktails """
    METHOD_CHOICES = [
        ('Shake/Strain', 'Shake/Strain'),
        ('Shake/Dump', 'Shake/Dump'),
        ('Stir/Strain', 'Stir/Strain'),
        ('Build', 'Build'),
    ]
    category = models.CharField(max_length=21,
                                choices=COCKTAIL_CATEGORY_CHOICES,
                                default='Levitate Menu')
    base_spirit = models.CharField(max_length=7,
                                   choices=BASE_SPIRIT_CHOICES,
                                   default='Bourbon')
    method = models.CharField(max_length=12,
                              choices=METHOD_CHOICES,
                              default='Shake/Strain')
    glassware = models.CharField(max_length=50, blank=True)
    bar_ingredients = models.ManyToManyField(BarRecipe, blank=True)
    spirit_ingredients = models.ManyToManyField(im.SpiritOrderItem, blank=True)
    garnish = models.CharField(max_length=50, blank=True)
