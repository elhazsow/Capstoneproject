from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class ViewTest(TestCase):
    def setUp(self):
        # Set up any necessary data for the test
        self.client = APIClient(enforce_csrf_checks=True)  # Create a test client instance
        self.user = User.objects.create_user(username='testuser123', password='testpassword')  # Create a test user
        self.token = Token.objects.create(user=self.user)  # Create a token for the test user
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)  # Set the token in the request headers
        self.menu_item = {'title': 'Test Menu View', 'price': 9.99, 'inventory': 10}
        self.list_url = reverse('menu')
        self.detail_url = reverse('single_menu_item', kwargs={'pk':4}) 
     
    
    def test_create_menu_item(self):

        response = self.client.post(self.list_url, self.menu_item, format='json')
        # Check if the response is 201 Created
        self.assertEqual(response.status_code, 201)
        # Check if the menu item is created in the database
        self.assertEqual(response.data['title'], self.menu_item['title'])
        self.assertEqual(response.data['price'], str(self.menu_item['price']))
        self.assertEqual(response.data['inventory'], self.menu_item['inventory'])
        self.assertContains( self.client.get(self.list_url), 'Test Menu View')

             
    def test_getall(self):
        response = self.client.get(self.list_url)
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the menu item is in the response data
        # self.assertContains(response, 'Test Menu View')
        
       