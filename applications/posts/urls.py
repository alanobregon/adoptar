from django.urls import path
from . import views

app_name= "posts"
urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("add/", views.PostCreateView.as_view(), name="add"),

    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.PostUpdateView.as_view(), name="update"),
    path("<int:pk>/cancel", views.PostCancelDeleteView.as_view(), name="cancel"),
    path("<int:pk>/postulate", views.PostulateToPostCreateView.as_view(), name="postulate"),
    path("<int:pk>/postulations", views.PostulationsFromPostListView.as_view(), name="postulations"),
    path("postulate/done", views.PostulationDoneTemplateView.as_view(), name="postulation_done"),

    path("postulations/<int:pk>/", views.ApproveCandidateView, name="approve_postulation"),

    path("my/", views.CurrentUserPostListView.as_view(), name="my_publications"),
    path("my/postulations", views.PostulationListView.as_view(), name="my_postulations"),
    path("category/<str:category>", views.SearchPostByCategoryListView.as_view(), name="category_search"),
]
