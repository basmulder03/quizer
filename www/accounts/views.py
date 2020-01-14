from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from accounts.forms import RegistrationForm
from django.views.generic import FormView


# Create your views here.
class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = '/'

    def post(self, request):
        if not User.objects.get(username=request.POST.get('username')).exists():
            return render(request, '404.html', {})
