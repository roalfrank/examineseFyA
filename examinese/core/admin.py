from django.contrib import admin
from  django.contrib.auth.models  import  Group 
from . import models

class  CuestionarioAdmin(admin.ModelAdmin):
    list_display=('titulo','descripcion','aleatorio')

class  Cuestionario_UsuarioAdmin(admin.ModelAdmin):
    list_display=('pk','cuestionario','usuario','completado')

class  PreguntasAdmin(admin.ModelAdmin):
    list_display=('titulo','cuestionario')

class  OpcionesAdmin(admin.ModelAdmin):
    list_display=('pregunta','titulo','correcta')

class  RespuestasAdmin(admin.ModelAdmin):
    list_display=('cuestionario','pregunta','opcion')
class  TipoAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion')


admin.site.site_header  =  "Fe y Acción Admin"  
admin.site.site_title  =  "Fe y Acción Admin"
admin.site.index_title  =  "Fe y Acción Admin"
admin.site.unregister(Group)
admin.site.register(models.Cuestionario,CuestionarioAdmin)
admin.site.register(models.Cuestionario_Usuario,Cuestionario_UsuarioAdmin)
admin.site.register(models.Preguntas,PreguntasAdmin)
admin.site.register(models.Opciones,OpcionesAdmin)
admin.site.register(models.Respuestas,RespuestasAdmin)
admin.site.register(models.Tipo,TipoAdmin)

