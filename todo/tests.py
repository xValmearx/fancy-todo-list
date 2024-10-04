from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Todo


# Create your tests here.


class BlogTest(TestCase):
    """Blog Tests"""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username="testsuer", email="test@email.com", password="secret")

        cls.todo = Todo.objects.create(name="bob", complete_by_datetime="10/9/2024")

    def test_post_model(self):
        self.assertEqual(self.todo.name, "bob")
        self.assertEqual(self.todo.complete_by_datetime, "10/9/2024")
        self.assertEqual(str(self.todo), "bob")

    def test_url_exist_at_correct_location_listview(self):
        """Test url exist at correct location listview"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        """test for correct template used"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_containes_correct_contents(self):
        """test to see pages contents"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "bob")
        self.assertContains(response, "10/9/2024")
