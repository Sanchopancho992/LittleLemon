from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.user = User.objects.create_user(username='test_user', password='123456')
    self.token = Token.objects.create(user=self.user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    self.menu1 = Menu.objects.create(title = "IceCream", price = 80, inventory = 100)
    self.menu2 = Menu.objects.create(title = "Pizza", price = 120, inventory = 50)
    self.menu3 = Menu.objects.create(title = "Burger", price = 90, inventory = 80)
    
  def test_get_all(self):
    url = reverse('menu')
    response = self.client.get(url)
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['count'], len(serializer.data))
    self.assertEqual(response.data['results'], serializer.data)