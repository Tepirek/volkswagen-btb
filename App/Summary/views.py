import io
import matplotlib.pyplot as plt
from django.db.models.fields.files import FieldFile
from django.http import FileResponse
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from django.db.models import Count
from App.helpers import log
from Point.models import Point
from BodyType.models import BodyType
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, serializers
from .serializers import SummaryGetSerializer, SummarySerializer, SummaryTypeSerializer
from .models import Summary
from rest_framework import status
from datetime import datetime
from django.core.files import File
from django.core.files.base import ContentFile


@api_view(['GET', 'POST'])
#@permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
#@permission_classes([IsOwnerOrSuperUser])
def summary_list(request, format=None):

    if request.method == 'GET':
        serializer = SummaryGetSerializer(data=request.query_params)
        if not serializer.is_valid():
            print(request.query_params)
            return Response(status=422)

        summaries = Summary.objects.filter(
            type=serializer.data['type'],
        )
        if serializer.data['date_from'] is not None:
            summaries = summaries.filter(
                date_start__gte=serializer.data['date_from'],
            )
        if serializer.data['date_to'] is not None:
            summaries = summaries.filter(
                date_end__lte=serializer.data['date_to'],
            )
        serializer = SummarySerializer(summaries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return generate_summary(request)

@api_view(['GET'])
#@permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
#@permission_classes([IsOwnerOrSuperUser])
def summary_detail(request, pk, format=None):
    
    try:
        summary = Summary.objects.get(pk=pk)
    except Summary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = SummarySerializer(summary)
    return Response(serializer.data)

    #Tutaj powinno byc tworzenie raportu?? [POST]


# Constants
PAGE_WIDTH, PAGE_HEIGHT = A4

font_name = 'Helvetica'
font_name_bold = 'Helvetica-Bold'
font_size_title = 28
font_size_subtitle = 18
font_size_date = 18
font_size_worker = 16


def generate_summary(request):

    serializer = SummaryGetSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=422)

    date_start = request.data['date_from']
    date_end =  request.data['date_to']

    date_start = datetime.strptime(date_start, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
    date_end = datetime.strptime(date_end, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')

    # Strt building the document
    filename = f'report_{date_start}-{date_end}.pdf'
    buf = io.BytesIO()
    c = canvas.Canvas(buf)
    c.setPageSize(landscape(A4))

    create_prolog(
        c,
        datetime.strptime(date_start, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'),
        datetime.strptime(date_end, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'),
    )

    # Creating plots 

    # Take all points which are interesting us
    # -> SELECT * FROM POINTS 
    #       INNER JOIN REPORTS ON 
    #           POINT.report_id == REPORT.id
    #               WHERE REPORT.created_at BETWEEN date_start AND date_end

    points = Point.objects.select_related('report').filter(report__created_at__gte=date_start).filter(report__created_at__lte=date_end)


    # Share of errors plot - bar 
    fig = share_of_errors_type_in_the_period(points, style='bar')
    add_image(c, fig, 'bar')
    #fig.close()

    # TOP most common error types - bar
    fig = top_error_types_in_the_period(points, 5)
    add_image(c, fig, 'bar')

    # Share of errors plot - pie
    fig = share_of_errors_type_in_the_period(points, style='pie')
    add_image(c, fig, 'pie')

    # Number of errors depending on the type of car body - bar
    fig = number_of_errors_in_body_types(points, style='bar')
    add_image(c, fig, 'bar')

    # Number of errors depending on the type of car body - pie
    fig = number_of_errors_in_body_types(points, style='pie')
    add_image(c, fig, 'pie')

    # Share of inclusions plot - bar 
    fig = share_of_inclusion_type_in_the_period(points, style='bar')
    add_image(c, fig, 'bar')

    # TOP most common inclusion types - bar
    fig = top_inclusion_types_in_the_period(points, 5)
    add_image(c, fig, 'bar')

    # Share of inclusions plot - pie
    fig = share_of_inclusion_type_in_the_period(points, style='pie')
    add_image(c, fig, 'pie')

    # Number of errors depending on the type of color - bar
    fig = number_of_errors_in_colors(points, style='bar')
    add_image(c, fig, 'bar')

    # Number of errors depending on the type of color - pie
    fig = number_of_errors_in_colors(points, style='pie')
    add_image(c, fig, 'pie')

    # Share of errors plot - bar 
    fig = number_of_errors_in_component_types(points, style='bar')
    add_image(c, fig, 'bar')

    # TOP most common error types - bar
    fig = top_component_types_with_errors(points, 5)
    add_image(c, fig, 'bar')

    # Share of errors plot - pie
    fig = number_of_errors_in_component_types(points, style='pie')
    add_image(c, fig, 'pie')

    # The best workers
    add_best_workers(c, points)

    #errors_location_on_body_types()

    # Save document
    c.save()

    data = {
        'file': File(buf, name=filename),
        'type': serializer.data['type'],
        'date_start': date_start,
        'date_end': date_end,
    }

    summarySerializer = SummarySerializer(data=data)
    if summarySerializer.is_valid():
        summarySerializer.save(
            created_by=request.user
        )
        log('addSummary', 'summary', True, request.user, summarySerializer.data['id'])
    else:
        return Response(data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # return FileResponse(buf, as_attachment=True, filename=f'Raport_{date_start}-{date_end}.pdf')
    return Response(status=status.HTTP_201_CREATED)

def create_prolog(c, date_start, date_end):

    c.setFillColorRGB(0,0,1)
    c.rect(0,0, PAGE_HEIGHT, PAGE_WIDTH, fill=1)
    c.setFillColorRGB(255,255,255)

    # Title
    title = "VOLKSWAGEN - BE THE BEST"
    title_width = stringWidth(title, font_name, font_size_title)
    title_y = PAGE_WIDTH/2.0 + 60

    # Subtitle
    subtitle = "RAPORT PODSUMOWUJACY OKRES:"
    subtitle_width = stringWidth(subtitle, font_name, font_size_subtitle)
    subtitle_y = PAGE_WIDTH/2.0

    # Date
    # TODO Pobranie i ustawienie daty z requesta
    date = date_start + " - " + date_end
    date_width = stringWidth(date, font_name_bold, font_size_date)
    date_y = PAGE_WIDTH/2.0 - 60

    # Add title
    textob = c.beginText((PAGE_HEIGHT - title_width) / 2.0, title_y)
    textob.setFont(font_name, font_size_title)
    textob.textLine(title)

    # Add subtitle
    textob.setFont(font_name, font_size_subtitle)
    textob.setTextOrigin((PAGE_HEIGHT - subtitle_width) / 2.0, subtitle_y)
    textob.textLine(subtitle)

    # Add date
    textob.setFont(font_name_bold, font_size_date)
    textob.setTextOrigin((PAGE_HEIGHT - date_width) / 2.0, date_y)
    textob.textLine(date)

    # Add prolog to the document
    c.drawText(textob)

    # End page
    c.showPage()


def add_image(c, fig, type='bar'):

    c.setFillColorRGB(0,0,1)
    c.rect(0,0, PAGE_HEIGHT, PAGE_WIDTH, fill=1)
    c.setFillColorRGB(255,255,255)

    # Insert plot into page
    imgdata = io.BytesIO()
    fig.savefig(imgdata, format='png', bbox_inches='tight', dpi=250)
    imgdata.seek(0)
    imgdata = ImageReader(imgdata)

    if type == 'pie':
        image_height = 500
        image_width =  500
    else:
        image_height = PAGE_HEIGHT - 275
        image_width =  PAGE_WIDTH - 275

    c.drawImage(imgdata, (PAGE_HEIGHT - image_height) / 2.0, (PAGE_WIDTH - image_width) / 2.0, image_height, image_width)
    
    c.showPage()


def add_best_workers(c, points):

    c.setFillColorRGB(52,58,235)
    c.rect(0,0, PAGE_HEIGHT, PAGE_WIDTH, fill=1)
    c.setFillColorRGB(255,255,255)

    list_of_workers = best_workers(points)

    text = 'NAJLEPSI PRACOWNICY'
    text_width = stringWidth(text, font_name, font_size_title)
    
    textob = c.beginText((PAGE_HEIGHT - text_width) / 2.0, PAGE_WIDTH - 150)
    textob.setFont(font_name, font_size_title)
    textob.textLine(text)

    c.drawText(textob)

    text_y = PAGE_WIDTH - 200
    iterator = 0

    for worker in list_of_workers:
        
        text = 'DLPX: ' + worker['report__created_by__worker_id'] + '   Imie: ' +  worker['report__created_by__first_name']
        text_width = stringWidth(text, font_name, font_size_worker)
        
        textob = c.beginText((PAGE_HEIGHT - text_width) / 2.0, text_y)
        textob.setFont(font_name, font_size_worker)
        textob.textLine(text)
        text_y -= 30
        iterator += 1

        if iterator % 5 == 0:
            c.drawText(textob)
            c.showPage()
            text_y = PAGE_WIDTH - 200

    c.drawText(textob)


# Functions to create plots 


def share_of_errors_type_in_the_period(points, style='bar'):

    results = points.values('error_type__name').annotate(total=Count('error_type')).order_by('total')

    names = list(map(lambda d: d['error_type__name'], results))
    values = list(map(lambda d: d['total'], results))
    
    if style == 'bar':
        fig = plt.figure(figsize=(15, 5))
        plt.xticks(rotation=45, ha='right')
        plt.bar(range(len(results)), values, tick_label=names)
        plt.ylabel('Liczba przypadków')
        plt.title('Ilość wystąpień poszczególnych błedów')
    else:
        fig = plt.figure(figsize=(7, 7))
        plt.pie(values, labels=names, autopct='%1.1f%%')
        plt.axis('equal')
        plt.tight_layout()
        plt.title('Ilość wystąpień poszczególnych błędów - wykres kołowy')

    return fig


def number_of_errors_in_body_types(points, style='bar'):
  
    results = points.select_related('report').values('report__body_type__name').annotate(total=Count('report__body_type')).order_by('total')
    
    names = list(map(lambda d: d['report__body_type__name'], results))
    values = list(map(lambda d: d['total'], results))
    
    if style == 'bar':
        fig = plt.figure(figsize=(15, 5))
        plt.xticks(rotation=45, ha='right')
        plt.bar(range(len(results)), values, tick_label=names)
        plt.ylabel('Liczba przypadków')
        plt.title('Ilość wystąpień błedów w zależności od typu karoserii')
    else:
        fig = plt.figure(figsize=(7, 7))
        plt.pie(values, labels=names, autopct='%1.1f%%')
        plt.axis('equal')
        plt.tight_layout()
        plt.title('Ilość wystąpień błędów w zależności od typu karoserii - wykres kołowy')

    return fig


def top_error_types_in_the_period(points, top):
    
    results = points.values('error_type__name').annotate(total=Count('error_type')).order_by('-total')[0:top]
    
    names = list(map(lambda d: d['error_type__name'], results))
    values = list(map(lambda d: d['total'], results))
    
    fig = plt.figure(figsize=(15, 5))
    plt.bar(range(len(results)), values, tick_label=names)
    plt.ylabel('Liczba przypadków')
    plt.title(f'TOP {top} najczęściej występujących typów błędów')

    return fig


def share_of_inclusion_type_in_the_period(points, style='bar'):
    results = points.values('inclusion_type__name').annotate(total=Count('inclusion_type')).order_by('total')

    names = list(map(lambda d: d['inclusion_type__name'], results))
    values = list(map(lambda d: d['total'], results))
    
    if style == 'bar':
        fig = plt.figure(figsize=(15, 5))
        plt.xticks(rotation=45, ha='right')
        plt.bar(range(len(results)), values, tick_label=names)
        plt.ylabel('Liczba przypadków')
        plt.title('Ilość wystąpień poszczególnych wtrąceń')
    else:
        fig = plt.figure(figsize=(7, 7))
        plt.pie(values, labels=names, autopct='%1.1f%%')
        plt.axis('equal')
        plt.tight_layout()
        plt.title('Ilość wystąpień poszczególnych wtrąceń - wykres kołowy')

    return fig


def top_inclusion_types_in_the_period(points, top):
    
    results = points.values('inclusion_type__name').annotate(total=Count('inclusion_type')).order_by('-total')[0:top]
    
    names = list(map(lambda d: d['inclusion_type__name'], results))
    values = list(map(lambda d: d['total'], results))
    
    fig = plt.figure(figsize=(15, 5))
    plt.bar(range(len(results)), values, tick_label=names)
    plt.ylabel('Liczba przypadków')
    plt.title(f'TOP {top} najczęściej występujących typów wtrąceń')

    return fig


def number_of_errors_in_colors(points, style='bar'):
  
    results = points.select_related('report').values('report__color__name').annotate(total=Count('report__color')).order_by('total')
    
    names = list(map(lambda d: d['report__color__name'], results))
    values = list(map(lambda d: d['total'], results))
    
    if style == 'bar':
        fig = plt.figure(figsize=(15, 5))
        plt.xticks(rotation=45, ha='right')
        plt.bar(range(len(results)), values, tick_label=names)
        plt.ylabel('Liczba przypadków')
        plt.title('Ilość wystąpień błedów w zależności od koloru')
    else:
        fig = plt.figure(figsize=(7, 7))
        plt.pie(values, labels=names, autopct='%1.1f%%')
        plt.axis('equal')
        plt.tight_layout()
        plt.title('Ilość wystąpień błędów w zależności od koloru - wykres kołowy')

    return fig


def number_of_errors_in_component_types(points, style='bar'):

    results = points.values('component_type__name').annotate(total=Count('component_type')).order_by('total')

    names = list(map(lambda d: d['component_type__name'], results))
    values = list(map(lambda d: d['total'], results))
    
    if style == 'bar':
        fig = plt.figure(figsize=(15, 5))
        plt.xticks(rotation=45, ha='right')
        plt.bar(range(len(results)), values, tick_label=names)
        plt.ylabel('Liczba przypadków')
        plt.title('Ilość wystąpień błędów na poszczególnych komponentach')
    else:
        fig = plt.figure(figsize=(7, 7))
        plt.pie(values, labels=names, autopct='%1.1f%%')
        plt.axis('equal')
        plt.tight_layout()
        plt.title('Ilość wystąpień błędów na poszczególnych komponentach - wykres kołowy')

    return fig


def top_component_types_with_errors(points, top):
    
    results = points.values('component_type__name').annotate(total=Count('component_type')).order_by('-total')[0:top]
    
    names = list(map(lambda d: d['component_type__name'], results))
    values = list(map(lambda d: d['total'], results))
    
    fig = plt.figure(figsize=(15, 5))
    plt.bar(range(len(results)), values, tick_label=names)
    plt.ylabel('Liczba przypadków')
    plt.title(f'TOP {top} komponentów z największą ilością błędów')

    return fig


def best_workers(points):

    results = points.select_related('report').values('report__created_by__worker_id', 'report__created_by__first_name', 'report__created_by__last_name').annotate(total=Count('report__created_by')).order_by('-total')

    if not len(results):
        return []

    max = results[0]['total']

    best_workers = []

    for result in results:
        if result['total'] == max:
            best_workers.append(result)

    return best_workers


def errors_location_on_body_types(points):

    body_types = BodyType.objects.all().values('name')

    for body_type in body_types:
        print(body_type['name'])

    pass


