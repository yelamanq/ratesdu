from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django import forms

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'shake'}),
            'password': forms.PasswordInput(attrs={'id': 'password'}),
        }

class ResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(),
        }

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))



