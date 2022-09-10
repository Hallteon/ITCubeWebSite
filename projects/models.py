from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=350, verbose_name='Название')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='projects', verbose_name='Автор')
    members = models.ManyToManyField(User, blank=True, verbose_name='Участники')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    public = models.BooleanField(default=False, auto_created=True, verbose_name='Публичный проект')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_id': self.pk})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

