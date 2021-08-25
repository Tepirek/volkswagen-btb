from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import InclusionType
from .serializers import InclusionTypeSerializer


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def inclusion_type_list(request, format=None):

    if request.method == 'GET':
        inclusion_types = InclusionType.objects.all()
        serializer = InclusionTypeSerializer(inclusion_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InclusionTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by=request.user,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def inclusion_type_detail(request, pk, format=None):
    
    try:
        inclusion_type = InclusionType.objects.get(pk=pk)
    except InclusionType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InclusionTypeSerializer(inclusion_type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InclusionTypeSerializer(inclusion_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inclusion_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)