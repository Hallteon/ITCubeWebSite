from django.shortcuts import render

from utils.utils import title


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная' + title})


def page_not_found(request, exception):
    return render(request, 'main/404.html', {'title': 'Старница не найдена' + title})