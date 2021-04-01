from .models import profile
from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class  UserRegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
        
        class Meta:
            model=profile
            fields=['image']