from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdateFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
class ProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
