from django.test import TestCase
from .models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(
            firstname="Daniel",
            lastname="Mohajer",
            date_of_birth="1996-06-06",
            phone_number="+989024278589",
            email="daniel.mohajer.mohacel@gmail.com",
            bank_account_number="123456789012"
        )

    def test_create_customer(self):
        """Ensure that we can create a new customer"""
        customer_count = Customer.objects.count()
        self.assertEqual(customer_count, 1)

    def test_unique_email(self):
        """Ensure email is unique"""
        with self.assertRaises(Exception):
            Customer.objects.create(
                firstname="Daniel",
                lastname="Mohajer",
                date_of_birth="1996-06-06",
                phone_number="+989024278589",
                email="daniel.mohajer.mohacel@gmail.com",
                bank_account_number="098765432109"
            )
