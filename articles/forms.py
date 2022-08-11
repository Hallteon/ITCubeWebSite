from django import forms


class AddArticleForm(forms.Form):
    title = forms.CharField(label="Название статьи", widget=forms.TextInput(attrs={'class': 'form-control form-input',
                                                                                   'placeholder': 'Введите ваше имя'}))
