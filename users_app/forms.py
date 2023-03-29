from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    #configuring form
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
