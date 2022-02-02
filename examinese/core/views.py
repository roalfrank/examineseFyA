import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Cuestionario, Cuestionario_Usuario, Preguntas, Respuestas,Tipo

LISTA_ALEATORIA=[]

@login_required()
def inicio(request):
    context={}
    context['title']='Libros de la serie Fe y Acción'
    context['sub_title']='Practicar los Examínese'
    context['tipos']= Tipo.objects.all()
    return render(request,'principal.html',context)

@login_required()
def libro(request,pk):
    context={}
    tipo = get_object_or_404(Tipo,pk=int(pk))
    context['title']=tipo.nombre
    context['sub_title']='Examínese'
    context['cuestionarios']= Cuestionario.objects.filter(tipo=tipo)
    return render(request,'libro.html',context)

@login_required()
def crear_examen(request,id_cuestionario):
    context={}
    cuestionario = get_object_or_404(Cuestionario,pk = id_cuestionario)
    usuario = request.user
    cuestionario_usuario = Cuestionario_Usuario(cuestionario=cuestionario,usuario=usuario)
    cuestionario_usuario.save()
    return  redirect(reverse('examinese:examen', kwargs={'pk': cuestionario_usuario.pk}))

@login_required()
def presentarPregunta(request,pk):
    global LISTA_ALEATORIA
    context={}
    cuestionario_usuario = get_object_or_404(Cuestionario_Usuario,pk=pk)
    if len(LISTA_ALEATORIA)>0:
        preguntas=LISTA_ALEATORIA
    else:
        if cuestionario_usuario.cuestionario.aleatorio:
            LISTA_ALEATORIA = Preguntas.objects.filter(cuestionario__tipo=cuestionario_usuario.cuestionario.tipo).values_list('pk',flat=True)
            preguntas=LISTA_ALEATORIA
            LISTA_ALEATORIA = Preguntas.objects.filter(cuestionario__tipo=cuestionario_usuario.cuestionario.tipo).values_list('id', flat=True)
            random_preguntas= random.sample(list(LISTA_ALEATORIA), min(len(LISTA_ALEATORIA), 5))
            LISTA_ALEATORIA = Preguntas.objects.filter(pk__in=random_preguntas)
            preguntas=LISTA_ALEATORIA
        else:
            preguntas = cuestionario_usuario.cuestionario.preguntas.all()
    paginator = Paginator(preguntas, 1) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if page_obj.number == page_obj.paginator.num_pages:
        LISTA_ALEATORIA=[]
    context['title']=cuestionario_usuario.cuestionario.titulo
    context['sub_title']=cuestionario_usuario.cuestionario.descripcion
    context['tipo']=cuestionario_usuario.cuestionario.tipo
    context['id_tipo']=cuestionario_usuario.cuestionario.tipo.pk
    context['page_obj']=page_obj
    context['cuestionario']=cuestionario_usuario.pk
    return render(request, 'vista_examen.html',context )


@login_required()
def resultadoCuestionario(request,pk):
    context={}
    cuestionario_usuario = get_object_or_404(Cuestionario_Usuario,pk=pk)
    respuestas = Respuestas.objects.filter(cuestionario__id=int(pk))
    cantidad_preguntas = respuestas.count()
    cantidad_respuestas_ok = respuestas.filter(opcion__correcta=True).count()
    cantidad_respuestas_no = respuestas.filter(opcion__correcta=False).count()
    if cantidad_respuestas_ok < (cantidad_preguntas - 2):
        aprobado=False
    else:
        aprobado=True
        cuestionario_usuario.completado=True
        cuestionario_usuario.save()
    context['title']=cuestionario_usuario.cuestionario.titulo
    context['sub_title']=cuestionario_usuario.cuestionario.descripcion
    context['cantidad_preguntas']=cantidad_preguntas
    context['respuestas']=respuestas
    context['cantidad_respuestas_ok']=cantidad_respuestas_ok
    context['cantidad_respuestas_no']=cantidad_respuestas_no
    context['aprobado']=aprobado
    context['tipo']=cuestionario_usuario.cuestionario.tipo
    context['id_tipo']=cuestionario_usuario.cuestionario.tipo.pk
    return render(request, 'resultado.html',context )

@login_required()
def procesarRespuesta(request):
    if request.method == 'POST':
       data={}
       print(request.POST)
       id_pregunta = int(request.POST['pregunta'])
       id_cuestionario = int(request.POST['cuestionario'])
       id_opcion = int(request.POST['opcion'])
       chequear_esta= Respuestas.objects.filter(
           cuestionario__id=id_cuestionario,
           pregunta__id=id_pregunta
       )
       print('Lista chequear :',chequear_esta)
       if len(chequear_esta)>=1:
           data['status']=0
           data['texto']='Ya el usuario a respondido esta pregunta'
           return JsonResponse(data, safe=False)
       else:
            try:
                Respuestas.objects.create(cuestionario_id=id_cuestionario,pregunta_id=id_pregunta,opcion_id=id_opcion)
            except Exception as e:
                print(e)
                print(e.args)
                print(type(e))
                data['status']=0
                data['texto']='Error creando la respuesta consultar al admin'
                return JsonResponse(data, safe=False)  
            data['status']=1
            return JsonResponse(data, safe=False)  
