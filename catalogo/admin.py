from django.contrib import admin

# Register your models here.
from.models import Usuario, Cerveza, Boleta, Compra

admin.site.register(Usuario)
admin.site.register(Cerveza)
admin.site.register(Boleta)
admin.site.register(Compra)
