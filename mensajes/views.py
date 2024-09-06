from django.shortcuts import render
from .forms import TableroForm

# Create your views here.

def home_view (request):
    tablero_form = TableroForm()
    return render(request,'home.html',{'form':tablero_form})

def eliminar_view (request):
    return render (request,'eliminar.html')

def ver_view (request):
    return render (request,'ver.html')
