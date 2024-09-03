from django.shortcuts import render

# Create your views here.

def home_view (request):
    return render("home.html")

def eliminar_view (request):
    return render ("eliminar.html")

def ver_view (request):
    return render ("ver.html")
