from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'account/index.html', {'param': 'hello', 'title': 'Django test'})
