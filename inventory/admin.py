from django.contrib import admin

from . import models as im


@admin.register(im.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(im.FoodOrderItem)
class FoodOrderItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'distributor', 'price_per_unit',
                    'current_inventory', 'item_par',
                    'all_categories', 'needs_ordering', 'last_updated_at']
    list_filter = ['area_categories__name', 'distributor__name',
                   'needs_ordering']
    list_editable = ['needs_ordering']
    search_fields = ['name', 'description']
    sortable_by = ['name', 'last_updated_at', 'distributor', 'categories']

    def price_per_unit(self, obj):
        return f'${obj.latest_price}'

    def item_par(self, obj):
        return f'{obj.par} {obj.unit}'

    def current_inventory(self, obj):
        return f'{obj.quantity_on_hand} {obj.unit}'

    def all_categories(self, obj):
        return ', '.join([c.name for c in obj.area_categories.all()])


@admin.register(im.SubRegion)
class SubRegionAdmin(admin.ModelAdmin):
    pass


@admin.register(im.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'all_sub_regions']

    def all_sub_regions(self, obj):
        return ', '.join([sr.name for sr in obj.sub_regions.all()])


@admin.register(im.Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'location']
    list_display_links = ['name']
    list_filter = ['category']

    def location(self, obj):
        return ', '.join([r.name for r in obj.regions.all()])


@admin.register(im.WineRegion)
class WineRegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'all_sub_regions']

    def all_sub_regions(self, obj):
        return ', '.join([sr.name for sr in obj.sub_regions.all()])


@admin.register(im.WineOrderItem)
class WineOrderItemAdmin(admin.ModelAdmin):
    list_display = ['full_wine_name', 'style',
                    'distributor', 'price_per_unit',
                    'current_inventory', 'item_par',
                    'all_categories', 'needs_ordering', 'last_updated_at']
    list_filter = ['area_categories__name', 'distributor__name',
                   'needs_ordering']
    list_editable = ['needs_ordering']
    search_fields = ['name', 'description']
    sortable_by = ['name', 'last_updated_at', 'distributor', 'categories']

    def full_wine_name(self, obj):
        return f'${obj.vintage} {obj.producer} {obj.name}'

    def price_per_unit(self, obj):
        return f'${obj.latest_price}'

    def item_par(self, obj):
        return f'{obj.par} {obj.unit}'

    def current_inventory(self, obj):
        return f'{obj.quantity_on_hand} {obj.unit}'

    def all_categories(self, obj):
        return ', '.join([c.name for c in obj.area_categories.all()])


@admin.register(im.SpiritOrderItem)
class SpiritOrderItemAdmin(admin.ModelAdmin):
    list_display = ['producer', 'name', 'category',
                    'distributor', 'price_per_unit',
                    'current_inventory', 'item_par',
                    'all_categories', 'needs_ordering', 'last_updated_at']
    list_filter = ['distributor__name', 'category',
                   'needs_ordering']
    list_editable = ['needs_ordering']
    search_fields = ['name', 'description']
    sortable_by = ['name', 'last_updated_at', 'distributor', 'categories']

    def full_wine_name(self, obj):
        return f'${obj.vintage} {obj.producer} {obj.name}'

    def price_per_unit(self, obj):
        return f'${obj.latest_price}'

    def item_par(self, obj):
        return f'{obj.par} {obj.unit}'

    def current_inventory(self, obj):
        return f'{obj.quantity_on_hand} {obj.unit}'

    def all_categories(self, obj):
        return ', '.join([c.name for c in obj.area_categories.all()])


@admin.register(im.BeerOrderItem)
class BeerOrderItemAdmin(admin.ModelAdmin):
    list_display = ['producer', 'name',
                    'distributor', 'price_per_unit',
                    'current_inventory', 'item_par',
                    'all_categories', 'needs_ordering', 'last_updated_at']
    list_filter = ['area_categories__name', 'distributor__name',
                   'needs_ordering']
    list_editable = ['needs_ordering']
    search_fields = ['name', 'description']
    sortable_by = ['name', 'last_updated_at', 'distributor', 'categories']

    def full_wine_name(self, obj):
        return f'${obj.vintage} {obj.producer} {obj.name}'

    def price_per_unit(self, obj):
        return f'${obj.latest_price}'

    def item_par(self, obj):
        return f'{obj.par} {obj.unit}'

    def current_inventory(self, obj):
        return f'{obj.quantity_on_hand} {obj.unit}'

    def all_categories(self, obj):
        return ', '.join([c.name for c in obj.area_categories.all()])
