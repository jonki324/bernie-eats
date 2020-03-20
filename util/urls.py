from django.urls import path
from . import views

app_name = 'util'

urlpatterns = [
    path('log/', views.log, name='log'),
    path('summary/', views.summary, name='summary'),
]
