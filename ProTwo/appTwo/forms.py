from django import forms
from appTwo.models import Users

class NewUserForm(forms.ModelForm):
    class Meta():
        model=Users
        fields="__all__"
