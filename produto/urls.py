from django.urls import path
from .views import listar_produtos, cadastrar_produto, modificar_produto, apagar_produto

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('new', cadastrar_produto, name='cadastrar_produto'),
    path('update/<int:id>/', modificar_produto, name='modificar_produto'),
    path('delete/<int:id>/', apagar_produto, name='apagar_produto'),
]