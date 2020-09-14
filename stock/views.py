from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from api.serializers.stock import ProdutoSerializer
from stock.repositories import ProdutoRepo


class ProdutoAPI(APIView):
    def get(self, request):
        produtos = ProdutoRepo.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class ProdutoDetailsAPI(APIView):
    def get(self, request, id_=None):
        instance = ProdutoRepo.by_id(id_)
        serializer = ProdutoSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id_=None):
        instance = ProdutoRepo.by_id(id_)
        serializer = ProdutoSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, id_=None):
        instance = ProdutoRepo.by_id(id_)
        instance.delete()
        return HttpResponse(status=204)

