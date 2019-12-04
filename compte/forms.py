from django import forms
from .models import Profile, User


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        fields = ['avatar', 'contact', 'info', 'address']
        model = Profile
        labels = {
            'info':'Information sur vous',
            'avatar':'Photo de profile',
        }


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
