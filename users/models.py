from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Ip(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ip', verbose_name='Пользователь')
    ip = models.CharField(max_length=100, null=True, verbose_name='Айпи')

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Айпи'
        verbose_name_plural = 'Айпи пользователей'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile', verbose_name='Пользователь')
    profile_picture = models.ImageField(default='images/profiles/default_profile.png', upload_to='images/profiles/', verbose_name='Аватар')
    xp = models.IntegerField(default=0, verbose_name='Опыт')
    slug = models.SlugField(null=True, max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_slug': self.slug})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'
