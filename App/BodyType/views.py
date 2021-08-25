from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import BodyType
from .serializers import BodyTypeSerializer


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def body_type_list(request, format=None):

    if request.method == 'GET':
        body_types = BodyType.objects.all()
        serializer = BodyTypeSerializer(body_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BodyTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by=request.user,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def body_type_detail(request, pk, format=None):
    
    try:
        body_type = BodyType.objects.get(pk=pk)
    except BodyType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BodyTypeSerializer(body_type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BodyTypeSerializer(body_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        body_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
