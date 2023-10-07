from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    return HttpResponse("<h1>Главная страница<h1>")


def greet(request):
    today_day = datetime.now().day
    today_month = datetime.now().month
    context = {'is_new_year': today_day == 1 and today_month == 1}
    return render(request, 'app/index.html', context)
