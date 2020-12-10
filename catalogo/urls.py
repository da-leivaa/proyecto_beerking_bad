from django.urls import path
from.views import home, album, carrito, login, nro_boleta, registrar, seguimiento

urlpatterns = [
    path('', home, name="home"),
    path('album/', album, name="album"),
    path('carrito/', carrito, name="carrito"),
    path('login/', login, name="login"),
    path('nro_boleta/', nro_boleta, name="nro_boleta"),
    path('registrar/', registrar, name="registrar"),
    path('seguimiento/', seguimiento, name="seguimiento"),
]

