from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import Color
from .serializers import ColorSerializer


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def color_list(request, format=None):

    if request.method == 'GET':
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by=request.user,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def color_detail(request, pk, format=None):
    
    try:
        color = Color.objects.get(pk=pk)
    except Color.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ColorSerializer(color)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ColorSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)