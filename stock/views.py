from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from stock.serializers import ProdutoSerializer
from stock.models import Produto


class ProdutoAPI(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class ProdutoDetailsAPI(APIView):
    def get(self, request, id_=None):
        instance = Produto.objects.all(id=id_)    #TODO: create repo
        serializer = ProdutoSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id_=None):
        instance = Produto.objects.all(id=id_)
        serializer = ProdutoSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, id_=None):
        instance = Produto.objects.all(id=id_)
        instance.delete()
        return HttpResponse(status=204)

