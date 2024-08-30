from uuid import uuid4

from django.test import TestCase

from . import models as dm


class DistributorTestCase(TestCase):
    def setUp(self):
        distributor = dm.Distributor.objects.create(
            name='Example Distributor',
            phone_number='(111) 123-4567',
            order_dates=''
        )

        dm.SalesRepresentative.objects.create(
            name='Example Sales Rep A',
            phone_number='',
            email='',
            distributor=distributor
        )

    def test_distributor_is_created_successfully(self):
        """ Ensure a distributor entity is created with correct fields """
        distributor = dm.Distributor.objects.first()

        self.assertEqual(type(distributor.id), type(uuid4()))
        self.assertEqual(distributor.name, 'Example Distributor')
        self.assertIsNot(type(distributor.phone_number), type(1))
        self.assertTrue(len(distributor.phone_number) < 19)
        self.assertIsNotNone(distributor.order_dates)

    def test_sales_rep_is_created_successfulyy(self):
        """ Ensure a sales rep entity is created with correct fields """
        sales_rep = dm.SalesRepresentative.objects.first()

        self.assertEqual(type(sales_rep.id), type(uuid4()))
        self.assertEqual(sales_rep.name, 'Example Sales Rep A')
        self.assertIsNot(type(sales_rep.phone_number), type(1))
        self.assertTrue(len(sales_rep.phone_number) < 19)
        self.assertEqual(sales_rep.distributor.name, 'Example Distributor')
