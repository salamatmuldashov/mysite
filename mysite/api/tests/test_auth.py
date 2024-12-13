from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class UserRegistrationTests(APITestCase):

    def setUp(self):
        self.url = '/api/auth/register/'
        self.valid_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'first_name': 'First',
            'last_name': 'Last',
        }

    def test_registration_successful(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user', response.data)

    def test_registration_missing_field(self):
        invalid_data = self.valid_data.copy()
        invalid_data.pop('username')
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserLoginTests(APITestCase):

    def setUp(self):
        self.url = '/api/auth/login/'
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword123'
        )

    def test_login_successful(self):
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'testpassword123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_credentials(self):
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
