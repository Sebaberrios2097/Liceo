from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Cursos.models import Almuerzo
from Almuerzos.serializers import AlmuerzoSerializer


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_almuerzos(request):
    if request.method == 'GET':
        listaAlmuerzos = Almuerzo.objects.all()
        serializer = AlmuerzoSerializer(listaAlmuerzos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = AlmuerzoSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_almuerzo(request, id):
    try:
        almuerzo = Almuerzo.objects.get(id_almuerzo = id)
    except Almuerzo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AlmuerzoSerializer(almuerzo)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AlmuerzoSerializer(almuerzo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
    elif request.method == 'DELETE':
        almuerzo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)