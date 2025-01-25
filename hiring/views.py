from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import  reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import forms, models


class RegisterView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'hiring/register.html'
    success_url = reverse_lazy('hiring:login')

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'hiring/login.html'

    def get_success_url(self):
        return reverse('hiring:user_list')

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('hiring:login')


class UserListView(ListView):
    template_name = 'hiring/user_list.html'
    context_object_name = 'user'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()
