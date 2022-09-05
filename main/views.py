from django.shortcuts import render
from django.views.generic import TemplateView


class ShowHomePage(TemplateView):
    template_name = 'main/index.html'


def page_not_found(request, exception):
    return render(request, 'main/404.html', {'title': 'Старница не найдена'})