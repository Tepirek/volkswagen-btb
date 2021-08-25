from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import Point
from .serializers import PointSerializer, PointSummarySerializer


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def point_list(request, format=None):
    if request.method == 'GET':
        points = Point.objects.filter(
            report=request.query_params['report']
        )
        serializer = PointSerializer(points, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by=request.user,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def summary_points(request, format=None):
    points = Point.objects\
        .filter(
            report=request.query_params['report']
        )\
        .values('error_type', 'inclusion_type', 'stage')\
        .order_by('stage')\
        .annotate(amount=Count('id'))

    serializer = PointSummarySerializer(points, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def point_detail(request, pk, format=None):
    try:
        point = Point.objects.get(pk=pk)
    except Point.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PointSerializer(point)
        return Response(serializer.data)


    elif request.method == 'DELETE':
        point.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
