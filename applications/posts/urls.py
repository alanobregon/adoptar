from django.urls import path
from . import views

app_name= "posts"
urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("add/", views.PostCreateView.as_view(), name="add"),
    path("my/", views.CurrentUserPostListView.as_view(), name="my_publications"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.PostUpdateView.as_view(), name="update"),
    path("category/<str:category>", views.SearchPostByCategoryListView.as_view(), name="category_search"),
]
