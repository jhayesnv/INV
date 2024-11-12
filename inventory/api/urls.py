from django.urls import path

from .views import (SpiritOrderItemListView,
                    SpiritOrderItemDetailView)

urlpatterns = [
    path('spirits', SpiritOrderItemListView.as_view(), name='spirits'),
    path('spirits/<pk>', SpiritOrderItemDetailView.as_view(), name='spirit'),
]
