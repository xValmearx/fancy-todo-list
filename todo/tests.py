from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Todo


# Create your tests here.


class BlogTest(TestCase):
    """Blog Tests"""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username="testsuer", email="test@email.com", password="secret")

        cls.todo = Todo.objects.create(name="bob", complete_by_datetime="10/9/2024")

    def test_post_model(self):
        self.assertEqual
