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

        item_C = im.FoodOrderItem.objects.create(
            name='White Granulated Sugar',
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

        simple = rm.BarRecipe.objects.create(
            name='Simple Syrup'
        )

        simple.ingredients.set([item_C])

        producer = im.Producer.objects.create(
            name="Michter's",
        )

        region = im.Region.objects.create(
            name='Kentucky'
        )

        whiskey = im.SpiritOrderItem.objects.create(
            name='Sour Mash',
            producer=producer,
            distributor=distributor,
            region=region
        )

        cocktail_item = rm.CocktailRecipe.objects.create(
            name='Old Fashioned'
        )

        cocktail_item.bar_ingredients.set([simple])
        cocktail_item.spirit_ingredients.set([whiskey])

    def test_menu_order_item_is_created_successfully(self):
        """ Ensure a menu item recipe is created with correct fields """
        menu_item = rm.MenuItemRecipe.objects.first()

        self.assertEqual(type(menu_item.id), type(uuid4()))
        self.assertEqual(menu_item.name, 'Stuffed Squid')
        self.assertEqual(menu_item.recipes.first().name,
                         'Asian Vinaigrette')
        self.assertTrue(len(menu_item.recipes.all()), 2)

    def test_cocktail_recipe_is_created_successfully(self):
        """ Ensure a cocktail recipe entity is created with correct fields """

        cocktail = rm.CocktailRecipe.objects.first()

        self.assertEqual(type(cocktail.id), type(uuid4()))
        self.assertEqual(cocktail.name, 'Old Fashioned')
        self.assertEqual(cocktail.category, 'Levitate Menu')
        self.assertEqual(cocktail.base_spirit, 'Bourbon')
        self.assertEqual(cocktail.method, 'Shake/Strain')
        self.assertIsNotNone(cocktail.spirit_ingredients)
        self.assertIsNotNone(cocktail.garnish)
