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

        # create food category and item entities
        food_category = im.Category.objects.create(
            name='Walk-in'
        )

        food_item = im.FoodOrderItem.objects.create(
            name='Butter Solid',
            distributor=distributor,
        )

        food_item.area_categories.set([food_category])

        # create a sub region entity
        im.SubRegion.objects.create(
            name='Chablis'
        )

        # create a region entity
        spain = im.Region.objects.create(
            name='Barcelona',
            area='Spain'
        )

        # create a producer entity
        producer = im.Producer.objects.create(
            name='Mark Ryan',
            category='Wine',
        )

        # create a grape entity
        cabernet = im.Grape.objects.create(
            name='Cabernet Sauvignon'
        )

        # create a wine order item entity
        wine_order_item = im.WineOrderItem.objects.create(
            name='Speed Racer Red',
            distributor=distributor,
            producer=producer,
            region=spain
        )

        wine_category = im.Category.objects.create(
            name='Wine',
            area='Bar'
        )

        wine_order_item.area_categories.set([wine_category])
        wine_order_item.grapes.set([cabernet])

        spirit_order_item = im.SpiritOrderItem.objects.create(
            name='Example Spirit',
            distributor=distributor,
            producer=producer,
            region=spain
        )

        spirit_category = im.Category.objects.create(
            name='Whiskey',
            area='Bar'
        )

        spirit_order_item.area_categories.set([spirit_category])

        beer_order_item = im.BeerOrderItem.objects.create(
            name='Example Beer',
            distributor=distributor,
            producer=producer,
            region=spain
        )

        beer_category = im.Category.objects.create(
            name='Beer',
            area='Bar'
        )

        beer_order_item.area_categories.set([beer_category])

    def test_food_order_item_is_created_successfully(self):
        """ Ensure a food order item entity is created with correct fields """

        item = im.FoodOrderItem.objects.first()

        self.assertEqual(type(item.id), type(uuid4()))
        self.assertEqual(item.name, 'Butter Solid')
        self.assertIsNotNone(item.description)
        self.assertIsNotNone(item.product_identifier)
        self.assertEqual(item.area_categories.first().name, 'Walk-in')
        self.assertEqual(item.par, 1.0)
        self.assertEqual(item.quantity_on_hand, 0.0)
        self.assertEqual(item.unit, 'cs')
        self.assertEqual(item.latest_price, 0.0)
        self.assertEqual(item.distributor.name, 'Example Distributor')

    def test_sub_region_is_created_successfully(self):
        """ Ensure a sub region is created as an ext of the base region """

        sub_region = im.SubRegion.objects.first()

        self.assertEqual(type(sub_region.id), type(uuid4()))
        self.assertEqual(sub_region.name, 'Chablis')

    def test_region_is_created_successfully(self):
        """ Ensure a region entity is created with correct fields """

        region = im.Region.objects.first()

        self.assertEqual(type(region.id), type(uuid4()))
        self.assertEqual(region.name, 'Barcelona')
        self.assertEqual(region.area, 'Spain')
        self.assertIsNotNone(region.sub_regions)

    def test_producer_is_created_successfully(self):
        """ Ensure a producer entity is created with correct fields """

        producer = im.Producer.objects.first()

        self.assertEqual(type(producer.id), type(uuid4()))
        self.assertEqual(producer.name, 'Mark Ryan')
        self.assertIsNotNone(producer.description)

    def test_grape_is_created_successfully(self):
        """ Ensure a grape entity is created with correct fields """

        grape = im.Grape.objects.first()

        self.assertEqual(type(grape.id), type(uuid4()))
        self.assertEqual(grape.name, 'Cabernet Sauvignon')
        self.assertEqual(grape.color, 'Red')
        self.assertIsNotNone(grape.description)

    def test_wine_order_item_is_created_successfully(self):
        """ Ensure a wine order item entity is created with correct fields """

        wine_order_item = im.WineOrderItem.objects.first()

        self.assertEqual(type(wine_order_item.id), type(uuid4()))
        self.assertEqual(wine_order_item.name, 'Speed Racer Red')
        self.assertEqual(wine_order_item.distributor.name,
                         'Example Distributor')
        self.assertEqual(wine_order_item.area_categories.first().name, 'Wine')
        self.assertEqual(wine_order_item.unit, 'cs')
        self.assertIsNotNone(wine_order_item.vintage)
        self.assertEqual(wine_order_item.producer.name, 'Mark Ryan')
        self.assertEqual(wine_order_item.grapes.first().name,
                         'Cabernet Sauvignon')
        self.assertEqual(wine_order_item.region.name, 'Barcelona')
        self.assertEqual(wine_order_item.style, 'Red')

    def test_spirit_order_item_is_created_successfully(self):
        """ Ensure a spirit order item entity is created w/ correct fields """

        spirit_order_item = im.SpiritOrderItem.objects.first()

        self.assertEqual(type(spirit_order_item.id), type(uuid4()))
        self.assertEqual(spirit_order_item.name, 'Example Spirit')
        self.assertEqual(spirit_order_item.distributor.name,
                         'Example Distributor')
        self.assertEqual(spirit_order_item.area_categories.first().name,
                         'Whiskey')
        self.assertEqual(spirit_order_item.unit, 'btl')
        self.assertEqual(spirit_order_item.producer.name, 'Mark Ryan')
        self.assertEqual(spirit_order_item.region.name, 'Barcelona')

    def test_beer_order_item_is_created_successfully(self):
        """ Ensure a beer order item entity is created w/ correct fields """

        beer_order_item = im.BeerOrderItem.objects.first()

        self.assertEqual(type(beer_order_item.id), type(uuid4()))
        self.assertEqual(beer_order_item.name, 'Example Beer')
        self.assertEqual(beer_order_item.distributor.name,
                         'Example Distributor')
        self.assertEqual(beer_order_item.area_categories.first().name,
                         'Beer')
        self.assertEqual(beer_order_item.unit, 'keg')
        self.assertEqual(beer_order_item.format, 'Draft')
        self.assertEqual(beer_order_item.producer.name, 'Mark Ryan')
        self.assertEqual(beer_order_item.region.name, 'Barcelona')
