from django.test import TestCase
from restaurant.models import Menu  
from rest_framework import status
from rest_framework.test import APIClient


class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIClient()

        self.menu1 = Menu.objects.create(title="Pizza", price=10.99, inventory=10)
        self.menu2 = Menu.objects.create(title="Burger", price=5.49, inventory=5)
        self.menu3 = Menu.objects.create(title="Salad", price=7.99, inventory=7)

    def test_getall(self):
        self.setup()
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        expected_data = [
            {
                "id": self.menu1.id,
                "title": self.menu1.title,
                "price": self.menu1.price,
                "inventory": self.menu1.inventory,
            },
            {
                "id": self.menu2.id,
                "title": self.menu2.title,
                "price": self.menu2.price,
                "inventory": self.menu2.inventory,
            },
            {
                "id": self.menu3.id,
                "title": self.menu3.title,
                "price": self.menu3.price,
                "inventory": self.menu3.inventory,
            },
        ]

        self.assertEqual(response.json(), expected_data)
