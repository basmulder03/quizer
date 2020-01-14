from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.views.generic import FormView
from django.http import HttpResponseRedirect


# Create your views here.
class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})