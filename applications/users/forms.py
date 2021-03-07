from django.forms import forms
from django.contrib.auth.forms import UserCreationForm

from . import models

#Create your forms here
class UserRegiterForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'province',
            'password1',
            'password2'
        }
    
