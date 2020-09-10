from django.urls import path, include
from stock.views import ProdutoAPI, ProdutoDetailsAPI

api_v1 = [
    path('produtos/', ProdutoAPI.as_view())
]

urlpatterns = [
    path('v1/', include(api_v1))
]

