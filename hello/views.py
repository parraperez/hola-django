from django.shortcuts import render
from datetime import datetime

def home(request):
    contexto = {
        "nombre": "Django",
        "fecha": datetime.now()
    }
    return render(request, "hello/home.html", contexto)

