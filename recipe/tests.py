from uuid import uuid4

from django.test import TestCase

from . import models as rm
from distributor import models as dm
from inventory import models as im


class RecipeTestCase(TestCase):
    def setUp(self):
        distributor = dm.Distributor.objects.create(
            name='Example Distributor',
            phone_number='(111) 123-4567',
            order_dates=''
        )

        category = im.Category.objects.create(
            name='Pantry'
        )

        item_A = im.FoodOrderItem.objects.create(
            name='Sesame Oil',
            distributor=distributor
        )

        item_B = im.FoodOrderItem.objects.create(
            name='Rice Wine Vinegar',
            distributor=distributor
        )

        item_A.area_categories.set([category])
        item_B.area_categories.set([category])

        kitchen_recipe = rm.KitchenRecipe.objects.create(
            name='Asian Vinaigrette'
        )

        kitchen_recipe.ingredients.set([item_A, item_B])

        menu_item = rm.MenuItemRecipe.objects.create(
            name='Stuffed Squid'
        )

        menu_item.recipes.set([kitchen_recipe])

    def test_menu_order_item_is_created_successfully(self):
        """ Ensure a menu item recipe is created with correct fields """
        menu_item = rm.MenuItemRecipe.objects.first()

        self.assertEqual(type(menu_item.id), type(uuid4()))
        self.assertEqual(menu_item.name, 'Stuffed Squid')
        self.assertEqual(menu_item.recipes.first().name,
                         'Asian Vinaigrette')
        self.assertTrue(len(menu_item.recipes.all()), 2)
