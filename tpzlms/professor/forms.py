from django import forms
from .import models

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = models.ProfessorDAL
        fields = "__all__"
 
