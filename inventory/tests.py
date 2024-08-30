from uuid import uuid4

from django.test import TestCase

from . import models as im
from distributor.models import Distributor


class InventoryTestCase(TestCase):
    def setUp(self):
        distributor = Distributor.objects.create(
            name='Example Distributor',
            phone_number='(111) 123-4567',
            order_dates=''
        )

        category = im.Category.objects.create(
            name='Walk-in'
        )

        item = im.FoodOrderItem.objects.create(
            name='Butter Solid',
            distributor=distributor,
        )

        item.categories.set([category])

    def test_food_order_item_is_created_successfully(self):
        """ Ensure a food order item entity is created with correct fields """

        item = im.FoodOrderItem.objects.first()

        self.assertEqual(type(item.id), type(uuid4()))
        self.assertEqual(item.name, 'Butter Solid')
        self.assertIsNotNone(item.description)
        self.assertIsNotNone(item.product_identifier)
        self.assertEqual(item.categories.first().name, 'Walk-in')
        self.assertEqual(item.par, 1.0)
        self.assertEqual(item.quantity_on_hand, 0.0)
        self.assertEqual(item.unit, 'cs')
        self.assertEqual(item.latest_price, 0.0)
        self.assertEqual(item.distributor.name, 'Example Distributor')
