from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView

from articles.models import Article


class ShowHomePage(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['articles_amount'] = Article.objects.filter(is_published=True).count
        context['users_amount'] = User.objects.count

        return context


def page_not_found(request, exception):
    return render(request, 'main/404.html', {'title': 'Старница не найдена'})