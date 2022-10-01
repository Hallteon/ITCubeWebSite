from django import forms

from notifications.models import ProjectApplication


class SendProjectApplicationForm(forms.ModelForm):
    class Meta:
        model = ProjectApplication
        fields = ('text',)
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control form-input form__input',
                                                 'placeholder': 'Введите текст заявки'})}