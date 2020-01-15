from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.core.validators import (
    validate_email,
    password
)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(min_length=4,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': True
    }))

    first_name = forms.CharField(min_length=2, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': True
    }))

    last_name = forms.CharField(min_length=2, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': True
    }))

    email = forms.EmailField(min_length=6, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'required': True
    }))

    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'required': True
    }))

    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'required': True
    }))

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
