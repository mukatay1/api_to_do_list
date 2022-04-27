from datetime import timezone

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Current, List
import datetime


# Create your tests here.
class CurrentListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example123', password='example123')
        self.current = Current.objects.create(title='Привычка', author=self.user, start=datetime.date.today(),
                                              end=datetime.date.today())

    def test_list(self):
        response = self.client.get(reverse('current_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        response = self.client.get(reverse('current_detail', kwargs={'pk': self.current.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example123', password='example123')
        self.list = List.objects.create(title='test', author=self.user, start=datetime.date.today())

    def test_list_list(self):
        response = self.client.get(reverse('list_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list(self):
        data = {
            'title': 'test',
            'author': self.user.pk,
            'start': datetime.date.today()
        }
        response = self.client.post(reverse('list_list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_detail(self):
        response = self.client.get(reverse('list_detail', kwargs={'pk': self.list.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
