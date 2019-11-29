from django.test import TestCase, Client
from .models import User


class CreateConversationTests(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(username='test', email='a@ali.com', password='qwerty')
        self.user2 = User.objects.create(username='test2', email='a@ali.com', password='qwerty')
        self.user3 = User.objects.create(username='test3', email='a@ali.com', password='qwerty')
        self.user4 = User.objects.create(username='test4', email='a@ali.com', password='qwerty')

    def test_valid_input(self):
        data = {
            "name": "second",
            "members": [
                self.user1.id,
                self.user2.id
            ]
        }
        c = Client()
        response = c.post('/chat/conversations/', data=data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_input(self):
        data = {
            "name": "second" * 1000,
            "members": [
                self.user1.id,
                self.user2.id,
                25908
            ]
        }
        c = Client()
        response = c.post('/chat/conversations/', data=data)
        self.assertEqual(response.status_code, 400)
