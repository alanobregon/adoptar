from django.urls import path
from . import views

app_name = "chats"

urlpatterns = [
    path("", views.ChatListView.as_view(), name="index"),
    path("<int:pk>/", views.ChatDetailView.as_view(), name="details"),
]
