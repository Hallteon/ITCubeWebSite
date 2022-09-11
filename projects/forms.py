from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from projects.models import Project


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'content', 'category', 'tags', 'public')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control form-input form__input',
                                                  'placeholder': 'Введите название проекта'}),
                   'content': CKEditorUploadingWidget(attrs={'class': 'form-control form-input form__input add-project-form__textarea',
                                                             'placeholder': 'Введите текст статьи'}),
                   'category': forms.Select(attrs={'class': 'form-control form-input form__input form__space'}),
                   'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form__checkbox'}),
                   'public': forms.NullBooleanSelect(attrs={'class': 'form-control form-input form__input'})}