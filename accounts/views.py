from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import CustomAuthenticationForm
from django.shortcuts import redirect


# View for user signin
class Signin(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('/')


# View for user signout
class Signout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')