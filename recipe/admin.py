from django.contrib import admin

from . import models as rm


@admin.register(rm.BackUpRecipe)
class KitchenRecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'season', 'year']
    list_filter = ['season', 'year']
    search_fields = ['name', 'description']


@admin.register(rm.MenuItemRecipe)
class MenuItemRecipe(admin.ModelAdmin):
    list_display = ['name', 'is_brunch', 'is_social_hour',
                    'is_available']
    list_filter = ['season', 'year', 'is_brunch', 'is_social_hour',
                   'is_available']
    search_fields = ['name', 'description', 'recipes__name']
    list_editable = ['is_available']


@admin.register(rm.BarRecipe)
class BarRecipeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['season', 'year']
    search_fields = ['name', 'description']


@admin.register(rm.CocktailRecipe)
class CocktailRecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'base_spirit',
                    'method', 'glassware', 'garnish']
    list_filter = ['base_spirit']
    search_fields = ['name', 'description']
