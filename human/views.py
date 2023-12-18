from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Human
from .serializers import HumanSerializer
# Create your views here.


@api_view(['GET'])
def get_humans(request, pk=0):
    if pk == 0:
        queryset = Human.objects.all()
        serializer = HumanSerializer(queryset, many=True)
        return Response(serializer.data)
    else:
        try:
            human = Human.objects.get(pk=pk)
        except Human.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = HumanSerializer(human)
        return Response(serializer.data)

@api_view(['POST'])
def create_human(request):
    serializer = HumanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'PUT'])
def update_human(request, pk):
    try:
        human = Human.objects.get(pk=pk)
    except Human.DoesNotExist:
        return Response({'error': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)
    serializer = HumanSerializer(human, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_human(request, pk):
    try:
        human = Human.objects.get(pk=pk)
    except Human.DoesNotExist:
        return Response({'error': 'продукт не найден'}, status=status.HTTP_404_NOT_FOUND)
    human.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)