from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import Logger
from .serializers import LoggerSerializer


@api_view(['GET', 'POST'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def log_list(request, format=None):

    if request.method == 'GET':
        logs = Logger.objects.filter(
            created_by=request.user,
            is_visible=True,
        )
        serializer = LoggerSerializer(logs, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = LoggerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by=request.user,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def log_detail(request, pk, format=None):
    
    try:
        log = Logger.objects.get(pk=pk)
    except Logger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = LoggerSerializer(log)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = LoggerSerializer(log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
