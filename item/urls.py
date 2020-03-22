from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='index'),
    path('detail/<int:pk>', views.ItemDetailView.as_view(), name='detail'),
    path('add/', views.ItemCreateView.as_view(), name='add'),
    path('edit/', views.edit, name='edit'),
    path('rmv/', views.rmv, name='rmv'),
]
