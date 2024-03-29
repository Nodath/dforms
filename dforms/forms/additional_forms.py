from django import forms
from django.contrib.auth.forms import UserCreationForm
from .user_forms import CustomUserCreationForm
from django.contrib.auth.models import User


class SignUpForm(CustomUserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=200, required=False, help_text="will be required someday")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
