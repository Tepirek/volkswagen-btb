import io
from django.core.files import File
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from Point.models import Point
from .models import Report
from .serializers import ReportSerializer, BlueprintSerializer
from App.permissions import IsOwnerOrSuperUser
from App.helpers import log
from datetime import datetime
from PIL import Image


doka_mapping_inside = {
    'bok_prawy': {
        'offset_x': 211,
        'offset_y': 6,
        'width': 430,
        'height': 294,
        'rotation': 0,
    },
    'maska': {
        'offset_x': 9,
        'offset_y': 267,
        'width': 170,
        'height': 356,
        'rotation': -1,
    },
    'podloga': {
        'offset_x': 212,
        'offset_y': 305,
        'width': 429,
        'height': 278,
        'rotation': -1,
    },
    'bok_lewy': {
        'offset_x': 208,
        'offset_y': 593,
        'width': 431,
        'height': 296,
        'rotation': -2,
    },
    'dach': {
        'offset_x': 659,
        'offset_y': 307,
        'width': 286,
        'height': 285,
        'rotation': -1,
    },
    'drzwi_prawe_przednie': {
        'offset_x': 971,
        'offset_y': 3,
        'width': 204,
        'height': 297,
        'rotation': 0,
    },
    'drzwi_lewe_przednie': {
        'offset_x': 977,
        'offset_y': 599,
        'width': 197,
        'height': 294,
        'rotation': -2,
    },
    'drzwi_lewe': {
        'offset_x': 1184,
        'offset_y': 7,
        'width': 130,
        'height': 292,
        'rotation': 0,
    },

    'drzwi_prawe': {
        'offset_x': 1181,
        'offset_y': 604,
        'width': 133,
        'height': 293,
        'rotation': -2,
    },
    'klapka_wlewu': {
        'offset_x': 843,
        'offset_y': 667,
        'width': 95,
        'height': 200,
        'rotation': -2,
    },
    'sciana_tyl': {
        'offset_x': 1023,
        'offset_y': 307,
        'width': 292,
        'height': 281,
        'rotation': -1,
    },
}

doka_mapping_outside = {
    'bok_lewy': {
        'offset_x': 207,
        'offset_y': 5,
        'width': 742,
        'height': 299,
        'rotation': 0,
    },
    'maska': {
        'offset_x': 10,
        'offset_y': 269,
        'width': 172,
        'height': 355,
        'rotation': -1,
    },
    'klapka_wlewu': {
        'offset_x': 839,
        'offset_y': 664,
        'width': 101,
        'height': 203,
        'rotation': -2,
    },
    'bok_prawy': {
        'offset_x': 204,
        'offset_y': 590,
        'width': 754,
        'height': 302,
        'rotation': -2,
    },
    'drzwi_prawe_przednie': {
        'offset_x': 973,
        'offset_y': 599,
        'width': 203,
        'height': 299,
        'rotation': -2,
    },
    'drzwi_lewe_przednie': {
        'offset_x': 969,
        'offset_y': 2,
        'width': 206,
        'height': 299,
        'rotation': 0,
    },
    'drzwi_prawe': {
        'offset_x': 1181,
        'offset_y': 5,
        'width': 134,
        'height': 294,
        'rotation': 0,
    },
    'drzwi_lewe': {
        'offset_x': 1180,
        'offset_y': 604,
        'width': 133,
        'height': 293,
        'rotation': -2,
    },
    'sciana_tyl': {
        'offset_x': 1023,
        'offset_y': 301,
        'width': 296,
        'height': 296,
        'rotation': -1,
    },
    'podloga': {
        'offset_x': 242,
        'offset_y': 307,
        'width': 681,
        'height': 272,
        'rotation': 0,
    },
    'dach': {
        'offset_x': 397,
        'offset_y': 319,
        'width': 219,
        'height': 254,
        'rotation': -1,
    },
}

kasten_mapping_inside = {
    'drzwi_przesuwane': {
        'offset_x': 8,
        'offset_y': 3,
        'width': 200,
        'height': 263,
        'rotation': 0,
    },
    'bok_prawy': {
        'offset_x': 241,
        'offset_y': 5,
        'width': 712,
        'height': 259,
        'rotation': 0,
    },
    'drzwi_prawe_przednie': {
        'offset_x': 969,
        'offset_y': 1,
        'width': 207,
        'height': 303,
        'rotation': 0,
    },
    'drzwi_lewe': {
        'offset_x': 1177,
        'offset_y': 0,
        'width': 142,
        'height': 304,
        'rotation': 0,
    },
    'maska': {
        'offset_x': 7,
        'offset_y': 268,
        'width': 178,
        'height': 357,
        'rotation': -1,
    },
    'podloga': {
        'offset_x': 227,
        'offset_y': 312,
        'width': 754,
        'height': 279,
        'rotation': 0,
    },
    'klapka_wlewu': {
        'offset_x': 157,
        'offset_y': 739,
        'width': 83,
        'height': 160,
        'rotation': -2,
    },
    'bok_lewy': {
        'offset_x': 242,
        'offset_y': 633,
        'width': 710,
        'height': 260,
        'rotation': -2,
    },

    'drzwi_lewe_przednie': {
        'offset_x': 969,
        'offset_y': 600,
        'width': 205,
        'height': 299,
        'rotation': -2,
    },
    'drzwi_prawe': {
        'offset_x': 1175,
        'offset_y': 759,
        'width': 144,
        'height': 301,
        'rotation': -2,
    },
}

kasten_mapping_outside = {
    'drzwi_przesuwane': {
        'offset_x': 8,
        'offset_y': 3,
        'width': 201,
        'height': 266,
        'rotation': 0,
    },
    'bok_lewy': {
        'offset_x': 221,
        'offset_y': 4,
        'width': 735,
        'height': 306,
        'rotation': 0,
    },
    'drzwi_lewe_przednie': {
        'offset_x': 970,
        'offset_y': 1,
        'width': 206,
        'height': 300,
        'rotation': 0,
    },
    'drzwi_prawe': {
        'offset_x': 1178,
        'offset_y': 1,
        'width': 141,
        'height': 304,
        'rotation': 0,
    },
    'maska': {
        'offset_x': 10,
        'offset_y': 268,
        'width': 173,
        'height': 355,
        'rotation': -1,
    },
    'tyl': {
        'offset_x': 989,
        'offset_y': 303,
        'width': 330,
        'height': 296,
        'rotation': -1,
    },
    'klapka_wlewu': {
        'offset_x': 159,
        'offset_y': 739,
        'width': 82,
        'height': 160,
        'rotation': -2,
    },
    'bok_prawy': {
        'offset_x': 221,
        'offset_y': 591,
        'width': 728,
        'height': 300,
        'rotation': -2,
    },
    'drzwi_prawe_przednie': {
        'offset_x': 973,
        'offset_y': 600,
        'width': 200,
        'height': 299,
        'rotation': -2,
    },
    'drzwi_lewe': {
        'offset_x': 1175,
        'offset_y': 597,
        'width': 144,
        'height': 302,
        'rotation': -2,
    },
    'podloga': {
        'offset_x': 195,
        'offset_y': 303,
        'width': 729,
        'height': 276,
        'rotation': 0,
    },
}


@api_view(['GET', 'POST'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
@permission_classes([IsOwnerOrSuperUser])
def report_list(request, format=None):
    if request.method == 'GET':
        reports = Report.objects.filter(
            created_by=request.user
        )
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by=request.user,
            )
            log('addReport', 'report', True, request.user, serializer.data['id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
@permission_classes([permissions.IsAuthenticated, IsOwnerOrSuperUser])
def report_detail(request, pk, format=None):
    try:
        report = Report.objects.get(pk=pk)
    except Report.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data)


    elif request.method == 'PUT':
        report.state = 'done'
        report.sent_at = datetime.now()
        report.save()
        log('updateReport', 'report', True, request.user, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


    elif request.method == 'DELETE':
        log('deleteReport', 'report', True, request.user, pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#####################
# BLUEPRINT MAPPING #
#####################

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def blueprint(request, pk):
    try:
        report = Report.objects.get(pk=pk)
    except Report.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    report_id = report.id
    body_type = report.body_type

    points = Point.objects.select_related('report').filter(
        report=report_id,
        report__body_type=body_type.id,
    )

    original_inside = Image.open(body_type.blueprint_inside)
    original_outside = Image.open(body_type.blueprint_outside)

    copy_inside = original_inside.copy()
    copy_outside = original_outside.copy()

    for point in points:
        x = point.x
        y = point.y
        is_inner = point.component_type.is_inner
        component_name = point.component_type.name.lower().replace(' ', '_')
        marker = get_marker_image(point.error_type, point.inclusion_type)

        if is_inner:
            if body_type.id == 1:
                mapping = doka_mapping_inside[component_name]
            elif body_type.id == 2:
                mapping = kasten_mapping_inside[component_name]
            else:
                pass
            add_marker(copy_inside, marker, x, y, mapping)
        else:
            if body_type.id == 1:
                mapping = doka_mapping_outside[component_name]
            elif body_type.id == 2:
                mapping = kasten_mapping_outside[component_name]
            else:
                pass
            add_marker(copy_outside, marker, x, y, mapping)

    buf_inside = io.BytesIO()
    copy_inside.save(buf_inside, format='jpeg')

    buf_outside = io.BytesIO()
    copy_outside.save(buf_outside, format='jpeg')

    report.blueprint_inside=File(
        file=buf_inside,
        name=get_file_name('inside', body_type, report)
    )
    report.blueprint_outside=File(
        file=buf_outside,
        name=get_file_name('outside', body_type, report)
    )
    report.save()

    data = {
        'blueprint_inside': report.blueprint_inside,
        'blueprint_outside': report.blueprint_outside
    }

    reportSerializer = BlueprintSerializer(data=data)
    if reportSerializer.is_valid():
        return Response(reportSerializer.data)

    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_marker_image(error, inclusion):
    path = inclusion.marker if inclusion else error.marker
    return Image.open(path)


def add_marker(image, marker, x, y, mapping):
    new_x, new_y = get_position(x, y, mapping)
    offset = (
        int((mapping['offset_x'] + new_x + 3)),
        int((mapping['offset_y'] + new_y + 3))
    )
    image.paste(marker, offset)


def get_position(x, y, mapping):
    # rotation 1x left
    if mapping['rotation'] == -1:
        new_x = y * mapping['width'] / 100
        new_y = (-x * mapping['height'] / 100) + mapping['height']
    # rotation 2x left
    elif mapping['rotation'] == -2:
        new_x = (-x * mapping['width'] / 100) + mapping['width']
        new_y = (-y * mapping['height'] / 100) + mapping['height']
    else:
        new_x = x * mapping['width'] / 100
        new_y = y * mapping['height'] / 100
    return new_x, new_y


def get_file_name(side, body_type, report):
    return f'blueprint_{side}_{body_type.name}_{report.id}.jpg'