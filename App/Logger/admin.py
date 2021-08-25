from django.contrib import admin
from .models import Logger


class LoggerAdmin(admin.ModelAdmin):
   
    list_display = (
        'id',
        'action',
        'type',
        'is_visible',
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
            'Base data', {
                'fields': [
                    'action',
                    'type',
                    'is_visible',
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
        'id',
        'action',
        'type',
        'is_visible',
        'created_by',
        'created_at',
        'updated_at',
    )

    ordering = (
        'id',
    )

admin.site.register(Logger, LoggerAdmin)
