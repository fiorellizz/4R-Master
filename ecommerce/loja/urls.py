from django.urls import path
from . import views

urlpatterns = [
    path('loja/', views.homepage, name="homepage"),
    path('', views.homepage, name="homepage"),
    path('confirmar-compra/<int:produto_id>/', views.confirmar_compra, name="confirmar_compra"),
    path('verificar-compra/<int:produto_id>/', views.verificar_compra, name="verificar_compra"),
    path('finalizar-compra/<int:produto_id>/', views.finalizar_compra, name="finalizar_compra"),
    path('loja/produtos/', views.produtos, name='produtos'),
    path('gerenciarloja/', views.gerenciar_loja, name='gerenciar_loja'),
    path('exportarrelatorio/<str:relatorio>/', views.exportar_relatorio, name='exportar_relatorio'),
]