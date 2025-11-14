from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'user_type', 'location']
