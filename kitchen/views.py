from django.shortcuts import render, HttpResponse


def index(request):
    """注文管理画面"""
    return HttpResponse('index')


def upd(request):
    """注文ステータス変更処理"""
    return HttpResponse('update')
