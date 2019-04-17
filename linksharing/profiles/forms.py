from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'photo']

        def clean(self):

            form_data = self.cleaned_data
            user_email = self.cleaned_data.get('user_email')

            try:
                User.objects.get(email=user_email)

            except User.DoesNotExist as err:
                self.add_error('user_email', "Email already exists ! ")

            return form_data


