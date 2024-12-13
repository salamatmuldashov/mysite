from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from models import Order
from django.contrib.auth import get_user_model

class OrderTests(APITestCase):

    def setUp(self):
        self.url = '/api/orders/'
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword123'
        )
        self.valid_data = {
            'user_id': self.user.id,
            'status': 'pending',
        }

    def test_create_order_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'username': 'testuser'}
        
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user_id', response.data)
        self.assertEqual(response.data['user_id'], self.user.id)

    def test_create_order_user_not_found(self):
        invalid_data = self.valid_data.copy()
        invalid_data['user_id'] = 9999 
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
