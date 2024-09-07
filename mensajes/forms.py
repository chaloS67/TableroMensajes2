from django import forms
from .models import Tablero

class TableroForm(forms.ModelForm):

    
    class Meta:
       model = Tablero  ## se toma como base el modelo tablero para el form
       fields = ['remitente','destinatario','texto'] ## se agregan los campos que se toman del model Tablero