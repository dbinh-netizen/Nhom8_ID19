from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Custom user model to handle different roles
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model
User  = get_user_model()
# Player model for game interactions

# Developer model for game uploading
# Designer model for asset management

# Game model


# Game Asset model


# System Admin model


# Payment model for transactions

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    account_type = forms.ChoiceField(
        choices=User .ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','account_type']