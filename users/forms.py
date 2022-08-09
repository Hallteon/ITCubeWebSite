from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha import fields


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control form-input authorization-form__input',
                                                                                       'placeholder': 'Введите ваше имя'}))
    email = forms.CharField(label="Почта", widget=forms.EmailInput(attrs={'class': 'form-control form-input authorization-form__input',
                                                                          'placeholder': 'Введите вашу почту'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control form-input authorization-form__input',
                                                                                  'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-control form-input authorization-form__input',
                                                                                         'placeholder': 'Повоторите ваш пароль'}))
    captcha = fields.CaptchaField(label='Капча', widget=fields.CaptchaTextInput(attrs={'class': 'form-control form-input authorization-form__input authorization-form__input_captcha',
                                                                                       'placeholder': 'Введите текст с картинки'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control form-input authorization-form__input',
                                                                                       'placeholder': 'Введите ваше имя'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control form-input authorization-form__input',
                                                                                  'placeholder': 'Введите пароль'}))

    class Meta:
        fields = ('username', 'password')