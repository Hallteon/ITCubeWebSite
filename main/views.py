from django.shortcuts import render, redirect


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная'})