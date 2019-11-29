from django.test import TestCase, Client
from django.contrib.auth.models import User

from users.serializers import UserSerializer


class SignupTestCase(TestCase):
    def test_valid_signup(self):
        data = {'username': 'test',
                'password': 'test123',
                'first_name': 'ali',
                'last_name': 'ali',
                'email': 'ali.ghotbizadeh@gmail.com',
                }
        client = Client()
        response = client.post('/users/signup/', data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_signup(self):
        data = {'username': 't',
                'password': 'test123',
                'first_name': 'ali',
                'last_name': 'ali',
                'email': 'mailcom',
                }
        c = Client()
        response = c.post('/users/signup/', data)
        self.assertEqual(response.status_code, 400)

        data = {}
        response = c.post('/users/signup/', data)
        self.assertEqual(response.status_code, 400)


class UsersListTest(TestCase):
    def setUp(self):
        user1 = User(username='user1', password='qwerty')
        user2 = User(username='user2', password='qwerty')
        user3 = User(username='user3', password='qwerty')
        self.users = [user1, user2, user3]

    def test_users(self):
        c = Client()
        response = c.get('/users/list/')
        self.assertEqual(response.status_code, 200)
