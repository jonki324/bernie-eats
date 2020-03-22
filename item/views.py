from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Item


class ItemListView(LoginRequiredMixin, ListView):
    """商品一覧画面表示"""
    model = Item
    template_name = 'item/index.html'


class ItemCreateView(LoginRequiredMixin, CreateView):
    """商品追加処理"""
    model = Item
    template_name = 'item/create.html'
    fields = ('name', 'price', 'discount_price', 'comment', 'image')
    success_url = reverse_lazy('item:index')


class ItemDetailView(LoginRequiredMixin, DetailView):
    """商品詳細画面"""
    model = Item
    template_name = 'item/detail.html'

def detail(request):
    """商品詳細画面"""
    return HttpResponse('detail')


def edit(request):
    """商品編集処理"""
    return HttpResponse('edit')


def rmv(request):
    """商品削除処理"""
    return HttpResponse('rmv')
