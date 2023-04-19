from  django.test import TestCase 
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


class MenuViewTestCase(APITestCase):
     def test_get_all(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(serializer.data, response.data)
     def setUp(self):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Hamburger", Price=150, Inventory=200)
