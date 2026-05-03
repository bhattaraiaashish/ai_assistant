from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountViewTests(TestCase):
    def test_login_failure_stays_on_login_page(self):
        response = self.client.post(
            reverse("login"),
            {"username": "missing", "password": "wrong"},
            follow=True,
        )

        self.assertRedirects(response, reverse("login"))
        self.assertContains(response, "Invalid username or password.")

    def test_register_creates_user_and_redirects_to_login(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "aashish",
                "email": "aashish@example.com",
                "password": "StrongPass123!",
                "confirm_password": "StrongPass123!",
            },
        )

        self.assertRedirects(response, reverse("login"))
        self.assertTrue(User.objects.filter(username="aashish").exists())
