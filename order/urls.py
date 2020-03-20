from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check, name='check'),
    path('complete/', views.complete, name='complete'),
    path('status/', views.status, name='status'),
]
