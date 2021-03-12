from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
    
class UserUpdateProfileForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'province',
            'city',
            'avatar',
            'description'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = models.City.objects.none()

        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['city'].queryset = models.City.objects.filter(province=province_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.province:
            self.fields['city'].queryset = self.instance.province.city_set.order_by('name')

class UserReportForm(forms.ModelForm):
    reason = forms.ModelChoiceField(label="Razón", queryset=models.ReportReason.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))
    comment = forms.CharField(label="Descripción", max_length=200, required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Cuentanos que fue lo que sucedió'}))
    
    class Meta:
        model = models.UserReport
        fields = {
            'reason',
            'comment'
        }

class CalificateUserForm(forms.ModelForm):
    score_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    title = forms.CharField(label="Titulo", max_length=100, required=True)
    score = forms.IntegerField(label="Puntuación", required=True, max_value=5, min_value=1, widget=forms.RadioSelect(choices=score_choices, attrs={'class':'btn-check'}))

    comment = forms.CharField(label="Comentario", required=True, widget=forms.Textarea(attrs={
        'rows':3,
    }))
    class Meta:
        model = models.Qualification
        fields = {
            'title',
            'score',
            'comment',
        }
