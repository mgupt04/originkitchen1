# website/chatbot/urls.py

from django.urls import path
from .views import chat_page, chat_api

urlpatterns = [
    path("chat/", chat_page, name="chat_page"),   # For GET requests (displaying the chat UI)
    path("chat/api/", chat_api, name="chat_api"),   # For POST requests (processing chat messages)
]
