from django.shortcuts import render, HttpResponse


def index(request):
    """商品選択画面"""
    return HttpResponse('index')


def check(request):
    """注文確認画面"""
    return HttpResponse('check')


def complete(request):
    """注文完了画面"""
    return HttpResponse('complete')


def status(request):
    """注文ステータス確認画面"""
    return HttpResponse('status')
