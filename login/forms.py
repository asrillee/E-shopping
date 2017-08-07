from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    # first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserLoginForm(forms.Form):
    username = forms.CharField();
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
