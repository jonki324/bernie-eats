from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def index(request):
    """ログイン画面の表示"""
    redirect_to = request.GET.get(key='next', default='/order/')
    form = LoginForm(initial={'redirect_to': redirect_to})
    return render(request, 'account/index.html', {'form': form})


def login_view(request):
    """ログイン認証処理"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_to = form.cleaned_data['redirect_to']
                return redirect(redirect_to)
            else:
                form.add_error('username', 'ユーザー名かパスワードが違います。')
                form.add_error('password', '')
        return render(request, 'account/index.html', {'form': form})
    else:
        return redirect('/account/')


def logout_view(request):
    """ログアウト処理"""
    logout(request)
    return redirect('/account/')
