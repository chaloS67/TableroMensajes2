from django.shortcuts import render

# Create your views here.

def home_view (request):
    return render(request,'home.html')

def eliminar_view (request):
    return render (request,'eliminar.html')

def ver_view (request):
    return render (request,'ver.html')
