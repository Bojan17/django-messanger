from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import logout,login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic

from . import forms

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('posts:all')
    template_name = "accounts/login.html"

    def get_form(self, form_class=None):
        if form_class == None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())


    def form_valid(self, form):
        login(self.request, form.get.user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignUpView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('posts:all')
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        return super().form_valid(form)
