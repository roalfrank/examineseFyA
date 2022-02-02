from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
    nombre = models.CharField(max_length=500,verbose_name='nombre')
    descripcion = models.CharField(max_length=500,verbose_name='descripcion',default='lolo')

    class  Meta:  
        verbose_name_plural  =  "Tipo" 

    def __str__(self):
        return self.nombre
    
class Cuestionario(models.Model):
    titulo = models.CharField(max_length=50,verbose_name='Título')
    descripcion = models.CharField(max_length=500,verbose_name='Descripción')
    aleatorio = models.BooleanField(default=False,verbose_name='Aleatorio')
    usuarios=models.ManyToManyField(User, verbose_name='Usuarios',through='Cuestionario_Usuario')
    tipo = models.ForeignKey(Tipo,verbose_name='Tipo Cuestionario',on_delete=models.CASCADE,null=True,default=None)
    cant_preguntas = models.IntegerField(verbose_name='Cantidad Preguntas',default=0)
    cant_usuarios = models.IntegerField(verbose_name='Cantidad Usuarios',default=0)
    
    class  Meta:  
        verbose_name_plural  =  "Cuestionarios" 

    def __str__(self):
        return f"{self.titulo}-{self.tipo}"

class Preguntas(models.Model):
    titulo = models.CharField(max_length=500,verbose_name='Título')
    cuestionario=models.ForeignKey(Cuestionario, verbose_name="Cuestionario", on_delete=models.CASCADE,related_name='preguntas',default=1)
    cant_opciones = models.IntegerField(verbose_name='Cantidad Opciones',default=0)
    
    def __str__(self):
        return f"{self.cuestionario}-{self.titulo}"
    class  Meta:  
        verbose_name_plural  =  "Preguntas" 

class Opciones(models.Model):
    pregunta=models.ForeignKey(Preguntas, verbose_name="Pregunta", on_delete=models.CASCADE,related_name='opciones')
    titulo = models.CharField(max_length=500,verbose_name='Título')
    correcta=models.BooleanField("Es la correcta",default=False)
    def __str__(self):
        return f"{self.pregunta}-{self.titulo}-{self.correcta}"
    class  Meta:  
        verbose_name_plural  =  "Opciones" 

class Cuestionario_Usuario(models.Model):
    cuestionario=models.ForeignKey(Cuestionario, verbose_name="Cuestionario", on_delete=models.CASCADE)
    usuario=models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE,related_name='cuestionarios')
    cant_respuestas = models.IntegerField(verbose_name='Cantidad Respuestas',default=0)
    cant_correcta = models.IntegerField(verbose_name='Cantidad Respuestas Correctas',default=0)
    completado=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.cuestionario}-{self.usuario.username}"
    class  Meta:  
        verbose_name_plural  =  "Cuestionario_Usuarios" 
    
class Respuestas(models.Model):
    cuestionario=models.ForeignKey(Cuestionario_Usuario, verbose_name="Cuestionario", on_delete=models.CASCADE)
    pregunta=models.ForeignKey(Preguntas, verbose_name="Pregunta", on_delete=models.CASCADE)
    opcion=models.ForeignKey(Opciones, verbose_name="Opción", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.cuestionario}-{self.opcion}"
    class  Meta:  
        verbose_name_plural  =  "Respuestas" 
    
