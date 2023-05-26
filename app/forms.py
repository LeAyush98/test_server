from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    model = Person
    fields = "__all__"
