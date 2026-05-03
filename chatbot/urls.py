from django.urls import path
from .views import chatbot,clear_chat

urlpatterns = [
    path('chatbot/', chatbot, name='chatbot'),
    path("clear-chat/",clear_chat, name="clear_chat"),
]