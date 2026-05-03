from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import ChatMessage


class ChatbotViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            email="tester@example.com",
            password="StrongPass123!",
        )

    def test_chat_requires_login(self):
        response = self.client.get(reverse("chatbot"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response["Location"])

    @patch("chatbot.views.get_ai_response", return_value="**Hello** from AI")
    def test_chat_saves_user_message_and_response(self, mocked_ai):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("chatbot"),
            {"message": "Can you help me?"},
        )

        self.assertRedirects(response, reverse("chatbot"))
        self.assertEqual(ChatMessage.objects.count(), 1)
        chat = ChatMessage.objects.get()
        self.assertEqual(chat.message, "Can you help me?")
        self.assertIn("<strong>Hello</strong>", chat.response)
        mocked_ai.assert_called_once_with("Can you help me?")

    def test_clear_chat_requires_login(self):
        response = self.client.post(reverse("clear_chat"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response["Location"])
