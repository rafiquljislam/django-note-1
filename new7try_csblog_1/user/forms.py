from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserReigstationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class UserUpdateFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class ProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

