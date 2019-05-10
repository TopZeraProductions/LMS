from django import forms
from .import models

class AlunoForm(forms.ModelForm):

    class Meta:
        model = models.AlunoDAL
        fields = "__all__"
