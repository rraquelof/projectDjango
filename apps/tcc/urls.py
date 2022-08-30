from django.urls import path
from .views import *

urlpatterns = [
    path('', TccList.as_view(), name='index'),
    path('', TccCreate.as_view()),
    path('', TccUpdate.as_view()),
    path('', TccDelete.as_view()),
    path('', TccDetail.as_view() ),
    path('',AutorCreate.as_view()),

    path('dashboard/tccs/', TccListPorUsuario.as_view(), name='listar_tccs_usuario'),
    path('listar/tcc_autor/<int:autor>/', TccAutorList.as_view(), name='listar_tcc_autor'),
    path('detalhar/tcc/<int:pk>/', TccDetail.as_view(), name='detalhar_tcc'),
    
    path('criar/tcc/', TccCreate.as_view(), name='criar_tcc'),
    path('editar/tcc/<int:pk>/', TccUpdate.as_view(), name='editar_tcc'),
    path('deletar/tcc/<int:pk>/', TccDelete.as_view(), name='deletar_tcc'),

    path('criar/autor/', AutorCreate.as_view(), name='criar_autor'),
    path('editar/autor/<int:pk>/', AutorUpdate.as_view(), name='editar_autor'),
    path('deletar/autor/<int:pk>/', AutorDelete.as_view(), name='deletar_autor'),
    path('listar/autores/', AutorList.as_view(), name='listar_autores'),
    path('listar/dashboard/', TccListPorUsuario.as_view(), name='listar_tccs'),
    path('detalhar/usuarios/', TccListPorUsuario.as_view(), name='listar_usuarios'),

]