from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('rmv/', views.rmv, name='rmv'),
]
