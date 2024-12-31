from rest_framework import serializers

from inventory.models import SpiritOrderItem


class SpiritOrderItemListSerializer(serializers.ModelSerializer):
    producer = serializers.StringRelatedField()

    class Meta:
        model = SpiritOrderItem
        fields = ['id', 'producer', 'name', 'category', 'menu_price',
                  'is_well', 'is_one_ounce_pour']


class SpiritOrderItemDetailSerializer(serializers.ModelSerializer):
    producer = serializers.StringRelatedField()

    class Meta:
        model = SpiritOrderItem
        exclude = ['par', 'distributor', 'product_identifier',
                   'needs_ordering', 'last_updated_at', 'unit', 'latest_price']
