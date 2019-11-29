from django.urls import path

from .views import ConversationsView, ConversationView

urlpatterns = [
    path('conversations/', ConversationsView.as_view(), name='conversations'),
    path('conversation/<int:pk>/', ConversationView.as_view(), name='conversation-view'),
]