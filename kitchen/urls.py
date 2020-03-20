from django.urls import path
from . import views

app_name = 'kitchen'

urlpatterns = [
    path('', views.index, name='index'),
    path('upd/', views.upd, name='upd'),
]
