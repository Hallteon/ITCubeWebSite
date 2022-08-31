from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha import fields

from users.models import UserProfile


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control form-input form__input'}),
                   'password': forms.TextInput(attrs={'class': 'form-control form-input form__input'})}


class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'profile_picture',)
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control form-input form__input'}),
                   'profile_picture': forms.FileInput(attrs={'class': 'form-control form-input form__input'})}


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control form-input form__input',
                                                                                       'placeholder': 'Введите ваше имя'}))
    email = forms.CharField(label="Почта", widget=forms.EmailInput(attrs={'class': 'form-control form-input form__input',
                                                                          'placeholder': 'Введите вашу почту'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control form-input form__input',
                                                                                  'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-control form-input form__input',
                                                                                         'placeholder': 'Повоторите ваш пароль'}))
    captcha = fields.CaptchaField(label='Капча', widget=fields.CaptchaTextInput(attrs={'class': 'form-control form-input form__input form__input_captcha',
                                                                                       'placeholder': 'Введите текст с картинки'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control form-input form__input',
                                                                                       'placeholder': 'Введите ваше имя'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control form-input form__input',
                                                                                  'placeholder': 'Введите пароль'}))

    class Meta:
        fields = ('username', 'password')