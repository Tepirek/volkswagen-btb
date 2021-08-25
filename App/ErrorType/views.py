from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import ErrorType
from .serializers import ErrorTypeSerializer


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def error_type_list(request, format=None):

    if request.method == 'GET':
        error_types = ErrorType.objects.all()
        serializer = ErrorTypeSerializer(error_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ErrorTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by=request.user,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def error_type_detail(request, pk, format=None):
    
    try:
        error_type = ErrorType.objects.get(pk=pk)
    except ErrorType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ErrorTypeSerializer(error_type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ErrorTypeSerializer(error_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        error_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
