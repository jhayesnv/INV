from uuid import uuid4

from django.db import models

import inventory.models as im


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
    ingredients = models.ManyToManyField(im.FoodOrderItem)
    is_gluten_free = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)


class MenuItemRecipe(BaseRecipe):
    """ Aggregate recipes for menu items """
    recipes = models.ManyToManyField(KitchenRecipe)
    is_brunch = models.BooleanField(default=False)
    is_social_hour = models.BooleanField(default=False)
