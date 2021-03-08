from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views

from . import models
from . import forms

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

# Login Views
class UserLoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class UserLogoutView(auth_views.LogoutView):
    pass

# Create User Views
class UserRegisterCreateView(generic.CreateView):
    model = models.User
    form_class = forms.UserRegiterForm
    template_name = "users/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)

# Reset Password Views
class UserResetPasswordView(auth_views.PasswordResetView):
    template_name = 'users/reset_password/reset.html'
    email_template_name = 'users/reset_password/email.html'
    subject_template_name = 'users/reset_password/subject.txt'
    success_url = reverse_lazy('users:password_reset_done')

class UserResetPasswordDoneView(auth_views.PasswordResetDoneView):
    template_name = 'users/reset_password/done.html'

class UserResetPasswordConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'users/reset_password/confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')

class UserResetPasswordCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'users/reset_password/complete.html'

# Change Password Views
class UserChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'users/change_password/change.html'
    success_url = reverse_lazy('users:password_change_done')

class UserChangePasswordDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'users/change_password/done.html'

class UserProfileView(generic.DetailView):
    model = models.User
    template_name = 'users/profile.html'
    slug_field = 'username'
    context_object_name = 'profile'
