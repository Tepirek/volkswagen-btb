from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import ComponentType
from .serializers import ComponentTypeSerializer
from App.permissions import IsOwnerOrSuperUser


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated, IsOwnerOrSuperUser])
def component_type_list(request, format=None):

    if request.method == 'GET':
        component_types = ComponentType.objects.filter(
            body_type=request.query_params['body_type'],
        )
        serializer = ComponentTypeSerializer(component_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ComponentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by=request.user,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def component_type_detail(request, pk, format=None):
    
    try:
        component_type = ComponentType.objects.get(pk=pk)
    except ComponentType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ComponentTypeSerializer(component_type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ComponentTypeSerializer(component_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        component_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)