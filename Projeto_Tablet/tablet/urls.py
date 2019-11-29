from django.urls import path
from . import views

app_name = 'tablet'
urlpatterns = [
    path('index/', views.cria_pessoa, name='index'),
    path('consulta/', views.consulta_matricula, name='consulta'),
    path('cpfs/', views.get_lista_cpfs, name='cpfs'),
    path('nomes/', views.get_lista_nomes, name='nomes'),
    path('reset/', views.socilicitar_reset, name='reset'),
    path('senha_temporaria/', views.get_senha_temporaria, name='senha_temporaria'),
    path('alterar_senha/<str:chave_token>', views.alterar_senha, name='alterar_senha'),
]
