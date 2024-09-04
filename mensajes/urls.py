from django.urls import path
from mensajes import views

urlpatterns = [
   
    path('', views.home_view, name='home'),
    path('eliminar/', views.eliminar_view, name='eliminar'),
    path('ver/', views.ver_view, name='ver'),
]