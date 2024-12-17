from decimal import Decimal as Dec

from django.contrib import admin

from . import models as im


@admin.register(im.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(im.Update)
class UpdateAdmin(admin.ModelAdmin):
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


@admin.register(im.Grape)
class GrapeAdmin(admin.ModelAdmin):
    pass


@admin.register(im.Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_display_links = ['name']
    list_filter = ['category']


@admin.register(im.WineOrderItem)
class WineOrderItemAdmin(admin.ModelAdmin):
    list_display = ['full_wine_name', 'style',
                    'distributor', 'price_per_unit',
                    'menu_price_per_serving', 'cost', 'current_inventory',
                    'item_par', 'needs_ordering',
                    'last_updated_at', 'is_glass_pour', 'is_available',
                    'is_active']
    list_filter = ['distributor__name',
                   'needs_ordering', 'is_glass_pour']
    list_editable = ['needs_ordering', 'is_available', 'is_active']
    search_fields = ['name', 'description']
    sortable_by = ['name', 'last_updated_at', 'distributor', 'categories']

    def full_wine_name(self, obj):
        return f'{obj.vintage} {obj.producer} {obj.name}'

    def menu_price_per_serving(self, obj):
        return f'${obj.menu_price}'

    def price_per_unit(self, obj):
        return f'${obj.latest_price}'

    def cost(self, obj):
        if not obj.is_glass_pour:
            return f'{(obj.latest_price / obj.menu_price)*100:.2f}%'
        # account for ~5% loss; latest price per bottle
        return f'{((obj.latest_price / Dec(4.0))/obj.menu_price)*100:.2f}%'

    def item_par(self, obj):
        return f'{obj.par} {obj.unit}'

    def current_inventory(self, obj):
        return f'{obj.quantity_on_hand} {obj.unit}'


@admin.register(im.SpiritOrderItem)
class SpiritOrderItemAdmin(admin.ModelAdmin):
    list_display = ['full_spirit_name', 'category',
                    'distributor', 'price_per_unit',
                    'menu_price_per_serving', 'cost', 'current_inventory',
                    'item_par', 'needs_ordering',
                    'last_updated_at', 'is_available', 'is_active']
    list_filter = ['distributor__name', 'category', 'needs_ordering']
    list_editable = ['needs_ordering', 'is_available', 'is_active']
    search_fields = ['name', 'description']
    sortable_by = ['name', 'last_updated_at', 'distributor', 'categories']

    def full_spirit_name(self, obj):
        return f'{obj.producer} {obj.name}'

    def menu_price_per_serving(self, obj):
        return f'${obj.menu_price}'

    def price_per_unit(self, obj):
        return f'${obj.latest_price}'

    def cost(self, obj):
        if not obj.is_one_ounce_pour:
            # account for 1-2 oz. pours with ~5% loss; bottle latest price
            return f'{((obj.latest_price/Dec(12.0)/obj.menu_price))*100:.2f}%'
        return f'{((obj.latest_price/Dec(24.0)/obj.menu_price))*100:.2f}%'

    def item_par(self, obj):
        return f'{obj.par} {obj.unit}'

    def current_inventory(self, obj):
        return f'{obj.quantity_on_hand} {obj.unit}'


@admin.register(im.BeerStyleCategory)
class BeerStyleCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(im.BeerStyle)
class BeerStyleAdmin(admin.ModelAdmin):
    pass


@admin.register(im.BeerOrderItem)
class BeerOrderItemAdmin(admin.ModelAdmin):
    list_display = ['full_beer_name',
                    'distributor', 'price_per_unit',
                    'menu_price_per_serving', 'cost', 'current_inventory',
                    'item_par', 'needs_ordering',
                    'last_updated_at', 'is_available', 'is_active']
    list_filter = ['distributor__name',
                   'needs_ordering']
    list_editable = ['needs_ordering', 'is_available', 'is_active']
    search_fields = ['name', 'description']
    sortable_by = ['name', 'last_updated_at', 'distributor', 'categories']

    def full_beer_name(self, obj):
        return f'{obj.producer} {obj.name}'

    def menu_price_per_serving(self, obj):
        return f'${obj.menu_price}'

    def price_per_unit(self, obj):
        return f'${obj.latest_price}'

    def cost(self, obj):
        if obj.format != 'Draft':
            return f'{(obj.latest_price / obj.menu_price) * 100:.2f}%'
        # account for 124 16 oz. pours with loss at ~10%; keg latest price
        return f'{((obj.latest_price / Dec(110.0)) / obj.menu_price)*100:.2f}%'

    def item_par(self, obj):
        return f'{obj.par} {obj.unit}'

    def current_inventory(self, obj):
        return f'{obj.quantity_on_hand} {obj.unit}'
