from asyncio import log
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from mensajes.models import Tablero
from .forms import TableroForm

# Create your views here.

def home_view (request):
   
    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
           mensaje = form.save()  # Guarda el objeto en la base de datos
           return redirect('ver',mensaje_id= mensaje.id )
    else:
        form = TableroForm()
    

    return render(request,'home.html',{'form':form})



class MensajeDeleteView(DeleteView):
    model = Tablero
    success_url = reverse_lazy('ver_mensajes')

#def eliminar_view (request):
    #return render (request,'eliminar.html')

def ver_view (request, mensaje_id):   ## Muestra el mensaje grabado ##

    mensaje= get_object_or_404(Tablero, id=mensaje_id)
    return render (request,'ver.html', {'mensaje': mensaje})

def ver_mensajes_view (request, usuario):
    mensajes_recividos = Tablero.objects.filter(destinatario=usuario)
    mensajes_enviados = Tablero.objects.filter(remitente=usuario)
    mensajes = []
    for msj in mensajes_recividos:
        mensaje = {'usuario_2': msj.remitente,  'texto': msj.texto, 'tipo': "recivido", 'id': msj.id}
        mensajes.append(mensaje)
    for msj in mensajes_enviados:
        mensaje = {'usuario_2': msj.destinatario,  'texto': msj.texto, 'tipo': "enviado", 'id': msj.id}
        mensajes.append(mensaje)

    return render (request,'ver_mensajes.html', {'mensajes': mensajes, 'usuario':usuario})

def ver_mensajes (request): 
    usuario = request.POST.get('usuario') 
    return redirect(ver_mensajes_view, usuario=usuario)

def buscar_mensajes (request):
    return render(request,'buscar.html')