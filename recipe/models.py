from datetime import date
from uuid import uuid4

from django.db import models

import inventory.models as im
from app.utils.model_helpers import (COCKTAIL_CATEGORY_CHOICES,
                                     BASE_SPIRIT_CHOICES)


class BaseRecipe(models.Model):
    """ Abstract model for bar and kitchen recipes """
    SEASON_CHOICES = (
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    season = models.CharField(max_length=6,
                              choices=SEASON_CHOICES,
                              default='Winter')
    year = models.CharField(max_length=4, blank=True,
                            default=str(date.today().year))
    yields = models.CharField(max_length=25, blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Allergy(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Allergies'

    def __str__(self):
        return self.name


class BackUpRecipe(BaseRecipe):
    """ Recipes relating to the kitchen """
    ingredient_1 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='bur_ing_1')
    ingredient_1_quantity = models.CharField(max_length=25, blank=True)
    ingredient_2 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='bur_ing_2')
    ingredient_2_quantity = models.CharField(max_length=25, blank=True)
    ingredient_3 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='bur_ing_3')
    ingredient_3_quantity = models.CharField(max_length=25, blank=True)
    ingredient_4 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='bur_ing_4')
    ingredient_4_quantity = models.CharField(max_length=25, blank=True)
    ingredient_5 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='bur_ing_5')
    ingredient_5_quantity = models.CharField(max_length=25, blank=True)
    ingredient_6 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='bur_ing_6')
    ingredient_6_quantity = models.CharField(max_length=25, blank=True)
    ingredient_7 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='bur_ing_7')
    ingredient_7_quantity = models.CharField(max_length=25, blank=True)
    ingredient_8 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='bur_ing_8')
    ingredient_8_quantity = models.CharField(max_length=25, blank=True)
    ingredient_9 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='bur_ing_9')
    ingredient_9_quantity = models.CharField(max_length=25, blank=True)
    ingredient_10 = models.ForeignKey(im.FoodOrderItem,
                                      on_delete=models.CASCADE, blank=True,
                                      null=True, related_name='bur_ing_10')
    ingredient_10_quantity = models.CharField(max_length=25, blank=True)
    ingredient_11 = models.ForeignKey(im.FoodOrderItem,
                                      on_delete=models.CASCADE, blank=True,
                                      null=True, related_name='bur_ing_11')
    ingredient_11_quantity = models.CharField(max_length=25, blank=True)
    ingredient_12 = models.ForeignKey(im.FoodOrderItem,
                                      on_delete=models.CASCADE, blank=True,
                                      null=True, related_name='bur_ing_12')
    ingredient_12_quantity = models.CharField(max_length=25, blank=True)
    instruction_1 = models.TextField(blank=True)
    instruction_2 = models.TextField(blank=True)
    instruction_3 = models.TextField(blank=True)
    instruction_4 = models.TextField(blank=True)
    instruction_5 = models.TextField(blank=True)
    instruction_6 = models.TextField(blank=True)
    instruction_7 = models.TextField(blank=True)
    instruction_8 = models.TextField(blank=True)


class MenuItemRecipe(BaseRecipe):
    """ Aggregate recipes for menu items """
    backup_recipe_1 = models.ForeignKey(BackUpRecipe, blank=True,
                                        null=True, on_delete=models.CASCADE,
                                        related_name='mi_bur_1')
    backup_recipe_1_quantity = models.CharField(max_length=25, blank=True)
    backup_recipe_2 = models.ForeignKey(BackUpRecipe, blank=True,
                                        null=True, on_delete=models.CASCADE,
                                        related_name='mi_bur_2')
    backup_recipe_2_quantity = models.CharField(max_length=25, blank=True)
    backup_recipe_3 = models.ForeignKey(BackUpRecipe, blank=True,
                                        null=True, on_delete=models.CASCADE,
                                        related_name='mi_bur_3')
    backup_recipe_3_quantity = models.CharField(max_length=25, blank=True)
    backup_recipe_4 = models.ForeignKey(BackUpRecipe, blank=True,
                                        null=True, on_delete=models.CASCADE,
                                        related_name='mi_bur_4')
    backup_recipe_4_quantity = models.CharField(max_length=25, blank=True)
    backup_recipe_5 = models.ForeignKey(BackUpRecipe, blank=True,
                                        null=True, on_delete=models.CASCADE,
                                        related_name='mi_bur_5')
    backup_recipe_5_quantity = models.CharField(max_length=25, blank=True)
    backup_recipe_6 = models.ForeignKey(BackUpRecipe, blank=True,
                                        null=True, on_delete=models.CASCADE,
                                        related_name='mi_bur_6')
    backup_recipe_6_quantity = models.CharField(max_length=25, blank=True)
    ingredient_1 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='mi_ing_1')
    ingredient_1_quantity = models.CharField(max_length=25, blank=True)
    ingredient_2 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='mi_ing_2')
    ingredient_2_quantity = models.CharField(max_length=25, blank=True)
    ingredient_3 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='mi_ing_3')
    ingredient_3_quantity = models.CharField(max_length=25, blank=True)
    ingredient_4 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='mi_ing_4')
    ingredient_4_quantity = models.CharField(max_length=25, blank=True)
    ingredient_5 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='mi_ing_5')
    ingredient_5_quantity = models.CharField(max_length=25, blank=True)
    ingredient_6 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='mi_ing_6')
    ingredient_6_quantity = models.CharField(max_length=25, blank=True)
    ingredient_7 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='mi_ing_7')
    ingredient_7_quantity = models.CharField(max_length=25, blank=True)
    ingredient_8 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='mi_ing_8')
    ingredient_8_quantity = models.CharField(max_length=25, blank=True)
    instruction_1 = models.TextField(blank=True)
    instruction_2 = models.TextField(blank=True)
    instruction_3 = models.TextField(blank=True)
    instruction_4 = models.TextField(blank=True)
    instruction_5 = models.TextField(blank=True)
    instruction_6 = models.TextField(blank=True)
    instruction_7 = models.TextField(blank=True)
    instruction_8 = models.TextField(blank=True)
    is_brunch = models.BooleanField(default=False)
    is_social_hour = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    allergies = models.ManyToManyField(Allergy, blank=True)


class BarRecipe(BaseRecipe):
    """ Recipes relating to the bar """
    ingredient_1 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='br_ing_1')
    ingredient_1_quantity = models.CharField(max_length=25, blank=True)
    ingredient_2 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='br_ing_2')
    ingredient_2_quantity = models.CharField(max_length=25, blank=True)
    ingredient_3 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='br_ing_3')
    ingredient_3_quantity = models.CharField(max_length=25, blank=True)
    ingredient_4 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='br_ing_4')
    ingredient_4_quantity = models.CharField(max_length=25, blank=True)
    ingredient_5 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='br_ing_5')
    ingredient_5_quantity = models.CharField(max_length=25, blank=True)
    ingredient_6 = models.ForeignKey(im.FoodOrderItem,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='br_ing_6')
    ingredient_6_quantity = models.CharField(max_length=25, blank=True)
    instruction_1 = models.TextField(blank=True)
    instruction_2 = models.TextField(blank=True)
    instruction_3 = models.TextField(blank=True)
    instruction_4 = models.TextField(blank=True)
    instruction_5 = models.TextField(blank=True)
    instruction_6 = models.TextField(blank=True)


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
    food_ingredient_1 = models.ForeignKey(im.FoodOrderItem,
                                          on_delete=models.CASCADE, blank=True,
                                          null=True, related_name='cr_ing_1')
    food_ingredient_1_quantity = models.CharField(max_length=25, blank=True)
    food_ingredient_2 = models.ForeignKey(im.FoodOrderItem,
                                          on_delete=models.CASCADE, blank=True,
                                          null=True, related_name='cr_ing_2')
    food_ingredient_2_quantity = models.CharField(max_length=25, blank=True)
    food_ingredient_3 = models.ForeignKey(im.FoodOrderItem,
                                          on_delete=models.CASCADE, blank=True,
                                          null=True, related_name='cr_ing_3')
    food_ingredient_3_quantity = models.CharField(max_length=25, blank=True)
    food_ingredient_4 = models.ForeignKey(im.FoodOrderItem,
                                          on_delete=models.CASCADE, blank=True,
                                          null=True, related_name='cr_ing_4')
    food_ingredient_4_quantity = models.CharField(max_length=25, blank=True)
    bar_recipe_1 = models.ForeignKey(BarRecipe,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='cr_ing_5')
    bar_recipe_1_quantity = models.CharField(max_length=25, blank=True)
    bar_recipe_2 = models.ForeignKey(BarRecipe,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='cr_ing_6')
    bar_recipe_2_quantity = models.CharField(max_length=25, blank=True)
    bar_recipe_3 = models.ForeignKey(BarRecipe,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='cr_ing_7')
    bar_recipe_3_quantity = models.CharField(max_length=25, blank=True)
    bar_recipe_4 = models.ForeignKey(BarRecipe,
                                     on_delete=models.CASCADE, blank=True,
                                     null=True, related_name='cr_ing_8')
    bar_recipe_4_quantity = models.CharField(max_length=25, blank=True)
    spirit_ingredient_1 = models.ForeignKey(im.SpiritOrderItem,
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True, related_name='si_ing_1')
    spirit_ingredient_1_quantity = models.CharField(max_length=25,
                                                    blank=True)
    spirit_ingredient_2 = models.ForeignKey(im.SpiritOrderItem,
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True, related_name='si_ing_2')
    spirit_ingredient_2_quantity = models.CharField(max_length=25, blank=True)
    spirit_ingredient_3 = models.ForeignKey(im.SpiritOrderItem,
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True, related_name='si_ing_3')
    spirit_ingredient_3_quantity = models.CharField(max_length=25, blank=True)
    spirit_ingredient_4 = models.ForeignKey(im.SpiritOrderItem,
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True, related_name='si_ing_4')
    spirit_ingredient_4_quantity = models.CharField(max_length=25, blank=True)
    spirit_ingredient_5 = models.ForeignKey(im.SpiritOrderItem,
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True, related_name='si_ing_5')
    spirit_ingredient_5_quantity = models.CharField(max_length=25, blank=True)
    spirit_ingredient_6 = models.ForeignKey(im.SpiritOrderItem,
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True, related_name='si_ing_6')
    spirit_ingredient_6_quantity = models.CharField(max_length=25, blank=True)
    garnish = models.CharField(max_length=50, blank=True)
    instruction_1 = models.TextField(blank=True)
    instruction_2 = models.TextField(blank=True)
    instruction_3 = models.TextField(blank=True)
    instruction_4 = models.TextField(blank=True)
    instruction_5 = models.TextField(blank=True)
    instruction_6 = models.TextField(blank=True)
    instruction_7 = models.TextField(blank=True)
    instruction_8 = models.TextField(blank=True)
    current_menu_recipe = models.BooleanField(default=False)
