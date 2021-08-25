from django.contrib import admin
from .models import Summary


class SummaryAdmin(admin.ModelAdmin):
   
    list_display = (
        'id',
        'file',
        'type',
        'date_start',
        'date_end',
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
                    'file',
                    'type',
                ],
            },
        ),
        (
            'Date', {
                'fields': [
                    'date_start',
                    'date_end',
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
        'created_by',
        'created_at',
        'updated_at',
    )

    ordering = (
        'id',
    )

admin.site.register(Summary, SummaryAdmin)
