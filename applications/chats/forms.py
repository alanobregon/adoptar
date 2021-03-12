from django import forms
from . import models

# Create your forms here
class SendMessageForm(forms.ModelForm):
    message = forms.CharField(label="Mensaje", max_length=1000, required=True, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Escribe un mensaje',
    }))
    
    class Meta:
        model = models.Message
        fields = {
            'message'
        }
