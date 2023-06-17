from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    context = {}
    return render(request, 'firstapp/index.html', context)
