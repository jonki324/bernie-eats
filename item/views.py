from django.shortcuts import render, HttpResponse


def index(request):
    """商品一覧画面表示"""
    return HttpResponse('index')


def detail(request):
    """商品詳細画面"""
    return HttpResponse('detail')


def add(request):
    """商品追加処理"""
    return HttpResponse('add')


def edit(request):
    """商品編集処理"""
    return HttpResponse('edit')


def rmv(request):
    """商品削除処理"""
    return HttpResponse('rmv')
