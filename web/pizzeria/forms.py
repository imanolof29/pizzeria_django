from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        #los campos que apareceran en el formulario
        fields = ['comentario']