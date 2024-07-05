from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class register_form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2']

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        Model = CustomUser
        fields = ['username', 'old_password', 'new_password1', 'new_password2']
