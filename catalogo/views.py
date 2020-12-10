from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def album(request):
    return render(request, 'app/album.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def nro_boleta(request):
    return render(request, 'app/nro_boleta.html')

def registrar(request):
    return render(request, 'app/registrar.html')

def seguimiento(request):
    return render(request, 'app/seguimiento.html')



