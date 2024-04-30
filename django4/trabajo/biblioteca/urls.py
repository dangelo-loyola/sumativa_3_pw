from django.urls import path
from .views import index, accion, inicio_de_sesion, aventura, categoria, comentarios_de_clientes, contacto, estrategia, quienes_somos, registro_usuario, rol, terror, olvide_contraseña
from django.contrib import admin
from .views import ItemListCreate
from django.urls import path


urlpatterns = [
    path('', index, name='index'),  
    path('admin/', admin.site.urls),
    path('index/', index, name="index"), 
    path('accion/', accion, name="accion"),
    path('aventura/', aventura, name="aventura"),
    path('inicio-de-sesion/', inicio_de_sesion, name="inicio_de_sesion"),
    path('categoria/', categoria, name="categoria"),
    path('comentarios-de-clientes/', comentarios_de_clientes, name="comentarios_de_clientes"),
    path('contacto/', contacto, name="contacto"),
    path('estrategia/', estrategia, name="estrategia"),
    path('quienes-somos/', quienes_somos, name="quienes_somos"),
    path('registro-usuario/', registro_usuario, name="registro_usuario"),
    path('rol/', rol, name="rol"),
    path('terror/', terror, name="terror"),
    path('olvide_contraseña/', olvide_contraseña, name="olvide_contraseña"),
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    
]
