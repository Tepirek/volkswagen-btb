from django.contrib import admin
from .models import Point


class PointAdmin(admin.ModelAdmin):
   
    list_display = (
        'id',
        'x',
        'y',
        'error_type',
        'inclusion_type',
        'component_type',
        'report',
        'created_by',
        'created_at',
        'updated_at',
    )
    
    list_filter = (
        
    )

    fieldsets = (

    )

    fieldsets = (
        (
            'Coordinates', {
                'fields': [
                    'x',
                    'y',
                ],
            },
        ),
        (
            'Errors', {
                'fields': [
                    'error_type',
                    'inclusion_type',
                ],
            },
        ),
        (
            'Place', {
                'fields': [
                    'component_type',
                    'report',
                ],
            },
        ),
        (
            'Creation', {
                'fields': [
                    'created_by',
                ],
            },
        ),
    )

    search_fields = (
        'name',
        'created_by',
        'created_at',
        'updated_at',
    )

    ordering = (
        'id',
    )

admin.site.register(Point, PointAdmin)
