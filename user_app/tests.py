from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


# Create your tests here.
class LoginLogout(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example1', password='example123')

    def test_login(self):
        data = {
            'username': 'example1',
            'password': 'example123',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username='example1')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class RegistrationTestCase(APITestCase):
    def test_register(self):
        data = {
            'username': 'username1',
            'email': 'email123@gmail.com',
            'password': '2002iliyas2013x',
            'password1': '2002iliyas2013x',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
