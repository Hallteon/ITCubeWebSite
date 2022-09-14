from django.db import models
from django.urls import reverse

from categories.models import Category


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_articles', kwargs={'tag_slug': self.slug})

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name']
