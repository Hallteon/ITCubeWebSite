from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile', verbose_name='Пользователь')
    name = models.CharField(null=True, max_length=100, verbose_name='Имя профиля')
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