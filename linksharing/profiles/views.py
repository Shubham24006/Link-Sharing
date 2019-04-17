from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView
from .forms import RegistrationForm
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"


class Register(FormView):
    template_name = 'sign_up.html'
    form_class = RegistrationForm
    # success_url = '/'

    def form_valid(self, form):
        form.save()
        return render(request=self.request, template_name='login.html')

    def form_invalid(self, form):
        return render(request=self.request, template_name='sign_up.html', context={'form': form.errors})


def user_login(request):
    pass


def user_logout(request):
    pass


