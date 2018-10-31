from django import forms
from .import models

class DisciplinaForm(forms.ModelForm):

    class Meta:
        model = models.DisciplinaDAL
        fields = "__all__"
 
