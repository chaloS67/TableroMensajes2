from django.urls import path
from mensajes import views

urlpatterns = [
   

    path('', views.home_view, name='home'),
    ##path('eliminar/', views.eliminar_view, name='eliminar'),
    path('ver/<int:mensaje_id>/', views.ver_view, name='ver'),
    path('mensajes/usuario/<str:usuario>/', views.ver_mensajes_view, name='ver_mensajes'),
    ##path('eliminar_mensaje/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),
    path('ver_mensajes/', views.ver_mensajes, name='ver_mensajes'),
    path('eliminar_mensaje/<int:pk>/',views.MensajeDeleteView.as_view(), name='eliminar_mensaje'),

]