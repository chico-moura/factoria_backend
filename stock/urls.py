from django.urls import path
from stock.views import ProdutosAPI, ProdutoDetailsAPI, ContatoAPI, ContatoDetailsAPI


urlpatterns = [
    path('produtos/', ProdutosAPI.as_view()),
    path('produtos/<int:instance_id>/', ProdutoDetailsAPI.as_view()),
    path('contatos/', ContatoAPI.as_view()),
    path('contatos/<int:instance_id>/', ContatoDetailsAPI.as_view()),
]

