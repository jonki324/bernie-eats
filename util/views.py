from django.shortcuts import render, HttpResponse


def log(request):
    """注文ステータスログ表示"""
    return HttpResponse('log')


def summary(request):
    """売り上げ集計画面"""
    return HttpResponse('summary')
