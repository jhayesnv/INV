from django.contrib import admin

from . import models as im


@admin.register(im.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(im.FoodOrderItem)
class FoodOrderItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'distributor', 'price_per_unit',
                    'current_inventory', 'item_par', 'last_updated_at',
                    'all_categories']
    list_filter = ['categories__name', 'distributor__name']
    search_fields = ['name', 'description']
    sortable_by = ['name', 'last_updated_at', 'distributor', 'categories']

    def price_per_unit(self, obj):
        return f'${obj.latest_price}'

    def item_par(self, obj):
        return f'{obj.par} {obj.unit}'

    def current_inventory(self, obj):
        return f'{obj.quantity_on_hand} {obj.unit}'

    def all_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all()])