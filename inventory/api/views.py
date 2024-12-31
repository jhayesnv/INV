from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import (SpiritOrderItemListSerializer,
                          SpiritOrderItemDetailSerializer)
from inventory.models import SpiritOrderItem


class SpiritOrderItemListView(ListAPIView):
    model = SpiritOrderItem
    queryset = SpiritOrderItem.objects.all()
    serializer_class = SpiritOrderItemListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['producer', 'category', 'is_well', 'is_one_ounce_pour']
    search_fields = ['name', 'description', 'producer__name']


class SpiritOrderItemDetailView(RetrieveAPIView):
    model = SpiritOrderItem
    queryset = SpiritOrderItem.objects.all()
    serializer_class = SpiritOrderItemDetailSerializer
