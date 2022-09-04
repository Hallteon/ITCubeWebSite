from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='Автор')
    title = models.CharField(max_length=350, verbose_name='Заголовок')
    cover_image = models.ImageField(upload_to='images/article_covers/%Y/%m/%d/', blank=True, verbose_name='Обложка')
    content = RichTextUploadingField(verbose_name='Текст')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Категория')
    tags = models.ManyToManyField('Tag', verbose_name='Тэги')
    views_count = models.ManyToManyField(User, blank=True, related_name='views', verbose_name='Количество просмотров')
    is_published = models.BooleanField(default=False, auto_created=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    text = models.TextField(verbose_name='Текст')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-create_time']


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


