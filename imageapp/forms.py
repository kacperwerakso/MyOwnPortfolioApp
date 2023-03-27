from django.forms import ModelForm
from .models import Img

class ImgsForm(ModelForm):
    class Meta:
        model = Img
        fields = ['tytul', 'opis', 'photo']