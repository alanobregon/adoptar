from django import forms
from . import models

# Create your forms here
class CreatePostForm(forms.ModelForm):
    pet_name = forms.CharField(label="nombre mascota", max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    pet_age = forms.IntegerField(label="edad", required=True, min_value=0, widget=forms.NumberInput(attrs={'placeholder':'Edad (aprox.)'}))
    category = forms.ModelChoiceField(label="Categoria", queryset=models.Category.objects.all(), widget=forms.RadioSelect(attrs={'class':'btn-check'}), empty_label=None)
    description = forms.CharField(label="Descripción", max_length=5000, required=True, widget=forms.Textarea(attrs={
        'placeholder':'Describenos un poco acerca del animal, cuentanos porque lo quieres postular para adopción',
        'rows': 15,
        'onkeyup':'countChar(this)'}))  
    class Meta:
        model = models.Post
        fields = {
            'title',
            'description',
            'photo',
            'category',
            'pet_name',
            'pet_age'
        }

class ChangePostStatusForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = {
            'status'
        }
