from django.shortcuts import render, HttpResponse


def index(request):
    """ログイン画面の表示"""
    return render(request, 'account/index.html', {'param': 'hello', 'title': 'Django test'})


def login(request):
    """ログイン認証処理"""
    return HttpResponse('login')


def logout(request):
    """ログアウト処理"""
    return HttpResponse('logout')
