from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from projects.models import Project, ProjectApplication


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'content', 'category', 'tags', 'public')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control form-input form__input',
                                                  'placeholder': 'Введите название проекта'}),
                   'description': forms.Textarea(attrs={'class': 'form-control form-input form__input',
                                                        'placeholder': 'Введите описание проекта',
                                                        'rows': 6}),
                   'content': CKEditorUploadingWidget(attrs={'class': 'form-control form-input form__input add-project-form__textarea',
                                                             'placeholder': 'Введите текст проекта'}),
                   'category': forms.Select(attrs={'class': 'form-control form-input form__input'}),
                   'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form__checkbox'}),
                   'public': forms.NullBooleanSelect(attrs={'class': 'form-control form-input form__input'})}


class SendProjectApplicationForm(forms.ModelForm):
    class Meta:
        model = ProjectApplication
        fields = ('text',)
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control form-input form__input',
                                                 'placeholder': 'Введите текст заявки'})}