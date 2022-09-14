from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from categories.models import Category
from tags.models import Tag


class Project(models.Model):
    name = models.CharField(max_length=350, verbose_name='Название')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='projects', verbose_name='Автор')
    members = models.ManyToManyField(User, blank=True, verbose_name='Участники')
    description = models.CharField(blank=True, max_length=650, verbose_name='Описание')
    content = RichTextUploadingField(null=True, verbose_name='Текст')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    public = models.BooleanField(default=False, auto_created=True, verbose_name='Публичный проект')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_slug': self.slug})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

