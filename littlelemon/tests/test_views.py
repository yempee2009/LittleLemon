from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=150, inventory=30)

    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        client = APIClient()
        #response = client.get('/restaurant/menu/items')
        response = client.get('/restaurant/menu/items/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)