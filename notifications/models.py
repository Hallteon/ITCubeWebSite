from django.contrib.auth.models import User
from django.db import models

from projects.models import Project


class Notice(models.Model):
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст')
    create_time = models.DateTimeField(auto_now=True, verbose_name='Дата отправки')

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'


class ProjectApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', verbose_name='Автор')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications', verbose_name='Проект')
    text = models.TextField(verbose_name='Текст заявки')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

