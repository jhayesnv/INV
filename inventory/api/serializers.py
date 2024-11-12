from rest_framework.serializers import ModelSerializer

from inventory.models import SpiritOrderItem


class SpiritOrderItemListSerializer(ModelSerializer):
    model = SpiritOrderItem
    fields = ['id', 'producer', 'name', 'category', 'menu_price']


class SpiritOrderItemDetailSerializer(ModelSerializer):
    model = SpiritOrderItem
    exclude = ['par', 'distributor', 'product_identifier', 'needs_ordering',
               'last_updated_at', 'unit', 'area_categories', 'latest_price']
