from django.contrib import admin

from . import models as rm


@admin.register(rm.KitchenRecipe)
class KitchenRecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(rm.MenuItemRecipe)
class MenuItemRecipe(admin.ModelAdmin):
    list_display = ['name', 'all_recipes', 'is_brunch', 'is_social_hour']
    list_filter = ['recipes__name']
    search_fields = ['name', 'description', 'recipes__name']
    list_editable = ['is_brunch', 'is_social_hour']

    def all_recipes(self, obj):
        return ', '.join([r.name for r in obj.recipes.all()])


@admin.register(rm.BarRecipe)
class BarRecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(rm.CocktailRecipe)
class CocktailRecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'base_spirit',
                    'method', 'glassware', 'bar_ingredients',
                    'spirit_ingredients', 'garnish']
    list_filter = ['base_spirit']
    search_fields = ['name', 'description', 'bar_ingredients',
                     'spirit_ingredients']
