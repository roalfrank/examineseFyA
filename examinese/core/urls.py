from django.urls import path
from .views import libro,inicio,crear_examen,presentarPregunta,procesarRespuesta,resultadoCuestionario
app_name = "examinese"

urlpatterns = [
    path("", inicio, name="inicio"),
    path("libro/<int:pk>/", libro, name="libro"),
    path("crear-examen/<int:id_cuestionario>/", crear_examen, name="crear_examen"),
    path("examen/<int:pk>/", presentarPregunta, name="examen"),
    path("procesar-respuesta/", procesarRespuesta, name="procesar_espuesta"),
    path("resultado-examen/<int:pk>/", resultadoCuestionario, name="resultado_examen"),
]