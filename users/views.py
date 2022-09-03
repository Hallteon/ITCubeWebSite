from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from users.forms import RegisterUserForm, LoginUserForm, UserSettingsForm, ProfileSettingsForm
from users.models import UserProfile
from utils.utils import DataMixin

from django.shortcuts import render, redirect


def index(request):
    return render(request, 'users/index.html', {'title': 'Главная'})


def logout_user(request):
    logout(request)

    return redirect('home')


class UserSettings(LoginRequiredMixin, DataMixin, UpdateView):
    template_name = 'users/user_settings.html'
    form_class = UserSettingsForm

    def get_object(self, *args, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'profile_slug': self.request.user.userprofile.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Настройки пользователя')

        return dict(list(context.items()) + list(c_def.items()))


class ProfileSettings(LoginRequiredMixin, DataMixin, UpdateView):
    template_name = 'users/user_settings.html'
    form_class = ProfileSettingsForm

    def get_object(self, *args, **kwargs):
        return self.request.user.userprofile

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'profile_slug': self.request.user.userprofile.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Настройки профиля')

        return dict(list(context.items()) + list(c_def.items()))


class ShowUserProfile(LoginRequiredMixin, DataMixin, DetailView):
    model = UserProfile
    template_name = 'users/profile.html'
    slug_url_kwarg = 'profile_slug'
    context_object_name = 'profile'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Пользователь')

        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        UserProfile.objects.create(user=user, name=user.username, slug=user.username)
        login(self.request, user)

        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')