from django.contrib import admin
from .models import Cliente, Categoria

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre')

    admin.site.register(Categoria)
