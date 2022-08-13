from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from mptt.models import TreeForeignKey, MPTTModel


class Article(models.Model):
    username = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор')
    title = models.CharField(max_length=350, verbose_name='Заголовок')
    cover_image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=False, verbose_name='Обложка')
    content = models.TextField(verbose_name='Текст')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    category = TreeForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views_count = models.IntegerField(null=False, default=0, verbose_name='Количество просмотров')
    comments_count = models.IntegerField(null=False, default=0, verbose_name='Количество комментариев')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    is_published = models.BooleanField(default=False, auto_created=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')

    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


