from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from stock.repositories import ProdutoRepo
from stock.serializers import ProdutoSerializer


class APIViewMetaclass(APIView):

    class Meta:
        abstract = True

    repo = None
    serializer = None


class ManyInstancesAPI(APIViewMetaclass):

    http_method_names = ['get', 'head', 'options', 'trace']

    @classmethod
    def get(cls, request):
        instances = cls.repo.all()
        serializer = cls.serializer(instances, many=True)
        return Response(serializer.data, status=200)

    @classmethod
    def post(cls, request):
        serializer = cls.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class SingleInstanceAPI(APIViewMetaclass):

    def get(self, request, instance_id=None):
        instance = ProdutoRepo.by_id(instance_id)
        serializer = ProdutoSerializer(instance)
        return Response(serializer.data)

    def put(self, request, instance_id=None):
        instance = ProdutoRepo.by_id(instance_id)
        serializer = ProdutoSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, instance_id=None):
        instance = ProdutoRepo.by_id(instance_id)
        instance.delete()
        return HttpResponse(status=204)

