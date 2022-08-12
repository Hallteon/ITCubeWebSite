from django import forms
from mptt.forms import TreeNodeChoiceField

from articles.models import Category, Article


class AddArticleForm(forms.ModelForm):
    # image = forms.ImageField(label='Изображение статьи', upload_to='images/%Y/%m/%d/', widget=forms.ImageField(attrs={'class': ''}))
    # title = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control form-input',
    #                                                                                'placeholder': 'Введите название статьи'}))
    # content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control form-input',
    #                                                                       'placeholder': 'Введите текст статьи'}))
    # category = forms.ModelChoiceField(queryset=Category.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"

    class Meta:
        model = Article
        category = TreeNodeChoiceField(queryset=Category.objects.all())
        fields = ['title', 'cover_image', 'content', 'category']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control form-input form__input',
                                                   'placeholder': 'Введите название статьи'}),
                   'content': forms.Textarea(attrs={'class': 'form-control form-input form__input',
                                                    'placeholder': 'Введите текст статьи'})}

