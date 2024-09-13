from django.contrib import admin

from . import models as rm


@admin.register(rm.KitchenRecipe)
class KitchenRecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(rm.MenuItemRecipe)
class MenuItemRecipe(admin.ModelAdmin):
    list_display = ['name', 'all_recipes']
    list_filter = ['recipes__name']
    search_fields = ['name', 'description', 'recipes__name']

    def all_recipes(self, obj):
        return ', '.join([r.name for r in obj.recipes.all()])
