from django.urls import path

from .views import chatapi

urlpatterns = [
    path('getReply', chatapi, name='chat-api'),
]