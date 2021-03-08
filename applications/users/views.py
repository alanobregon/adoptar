from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

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
    success_url = reverse_lazy('users:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        valid = super(UserRegisterCreateView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(self.request, username=username, password=password)
        login(self.request, new_user)
        return valid

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
class UserChangePasswordView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'users/change_password/change.html'
    success_url = reverse_lazy('users:password_change_done')

class UserChangePasswordDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = 'users/change_password/done.html'

# User Report Views
class UserReportView(LoginRequiredMixin, generic.CreateView):
    model = models.UserReport
    form_class = forms.UserReportForm
    template_name = 'users/user_report/report.html'
    success_url = reverse_lazy('users:profile_report_done')
    slug_field = 'username'

    def form_valid(self, form):
        current_user = self.request.user
        profile_user = models.User.objects.get(username=self.kwargs['slug'])

        form.instance.from_user = current_user
        form.instance.to_user = profile_user
        return super(UserReportView, self).form_valid(form)

class UserReportDoneView(LoginRequiredMixin, generic.base.TemplateView):
    template_name = 'users/user_report/done.html'

# User Profile Views
class UserProfileView(LoginRequiredMixin, generic.DetailView):
    model = models.User
    template_name = 'users/profile.html'
    slug_field = 'username'
    context_object_name = 'profile'

class UserProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.User
    form_class = forms.UserUpdateProfileForm
    template_name = 'users/update.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'slug': self.request.user.username})

#AJAX
def load_cities(request):
    province_id = request.GET.get('province')
    cities = City.objects.filter(province=province_id).order_by('name')
    return render(request, 'users/cities_list_options.html', { 'cities': cities })
    
