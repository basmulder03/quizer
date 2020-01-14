from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    username.widget.attrs = {
        'class': 'form-control',
    }

    first_name = forms.CharField()
    first_name.widget.attrs = {
        'class': 'form-control'
    }

    last_name = forms.CharField()
    last_name.widget.attrs = {
        'class': 'form-control'
    }

    email = forms.EmailField()
    email.widget.attrs = {
        'class': 'form-control'
    }

    password1 = forms.CharField()
    password1.widget = forms.PasswordInput()
    password1.widget.attrs = {
        'class': 'form-control'
    }

    password2 = forms.CharField()
    password2.widget = forms.PasswordInput()
    password2.widget.attrs = {
        'class': 'form-control'
    }

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self.save(commit=False))
        user.first_name = cleaned_data['first_name']
        user.last_name = cleaned_data['last_name']
        user.email = cleaned_data['email']

        if (commit):
            user.save()

        return user
