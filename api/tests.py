from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.models import Person, Group


class TestPerson(TestCase):

    def setUp(self):
        self.first_person = Person.objects.create(firstname='test_name',
                                                  lastname='test_lastname',
                                                  email='test@gmail.com')
        self.data = {'firstname': 'test_name', 'lastname': 'test_lastname', 'email': 'test@gmail.com'}
        self.data_long_name = {'firstname': 'to_long_name_to_long_name',
                               'lastname': 'test_lastname',
                               'email': 'test@gmail.com'}

    def test_persons_list(self):
        response = self.client.get(reverse('persons'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_person_create(self):
        response = self.client.post(reverse('persons'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fail_person_create(self):
        response = self.client.post(reverse('persons'), self.data_long_name)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_person_detail(self):
        response = self.client.get(reverse('person_detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_person_detail(self):
        response = self.client.get(reverse('person_detail', kwargs={'pk': self.first_person.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('firstname'), 'test_name')


class TestGroup(TestCase):

    def setUp(self):
        self.first_group = Group.objects.create(name='test_name')
        self.data = {'name': 'test_name'}
        self.data_long_name = {'name': 'to_long_name_to_long_name'}

    def test_groups_list(self):
        response = self.client.get(reverse('groups'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_group_create(self):
        response = self.client.post(reverse('groups'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fail_group_create(self):
        response = self.client.post(reverse('groups'), self.data_long_name)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_group_detail(self):
        response = self.client.get(reverse('group_detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_group_detail(self):
        response = self.client.get(reverse('group_detail', kwargs={'pk': self.first_group.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'test_name')

