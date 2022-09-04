from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная'})


def page_not_found(request, exception):
    return render(request, 'main/404.html', {'title': 'Старница не найдена'})