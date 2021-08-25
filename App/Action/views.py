from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import Action
from .serializers import ActionSerializer


@api_view(['GET', 'POST'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def action_list(request, format=None):

    if request.method == 'GET':
        actions = Action.objects.all()
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by=request.user,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def action_detail(request, pk, format=None):
    
    try:
        action = Action.objects.get(pk=pk)
    except Action.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActionSerializer(action)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActionSerializer(action, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        action.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
