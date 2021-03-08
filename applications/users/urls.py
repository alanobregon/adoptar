from django.urls import path
from django.contrib.auth import views as authViews

from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),

    path("register/", views.UserRegisterCreateView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),

    # Reset password urls
    path("password_reset/", views.UserResetPasswordView.as_view(), name="password_reset"),
    path("password_reset/done/", views.UserResetPasswordDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.UserResetPasswordConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", views.UserResetPasswordCompleteView.as_view(), name="password_reset_complete"),

    # Password Change urls
    path("password_change/", views.UserChangePasswordView.as_view(), name="password_change"),
    path("password_change/done", views.UserChangePasswordDoneView.as_view(), name="password_change_done"),

    # User Profile
    path("<str:slug>/", views.UserProfileView.as_view(), name="profile"),
]
