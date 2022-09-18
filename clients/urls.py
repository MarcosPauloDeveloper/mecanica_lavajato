from django.urls import path
from . import views


urlpatterns = [
    path('', views.clients, name='clients'),
    path('atualiza_cliente/', views.att_cliente, name='atualiza_cliente')
]
