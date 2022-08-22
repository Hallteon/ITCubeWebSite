from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from articles.models import Category, Article


class AddArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Article
        fields = ['title', 'cover_image', 'content', 'tags']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control form-input form__input',
                                                   'placeholder': 'Введите название статьи'}),
                   'content': CKEditorUploadingWidget(attrs={'class': 'form-control form-input form__input add-article-form__textarea',
                                                             'placeholder': 'Введите текст статьи'}),
                   'cover_image': forms.FileInput(attrs={'class': 'form-control form-input form__file-btn'}),
                   'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form__checkbox'})}


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'
