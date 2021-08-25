from django.contrib import admin
from .models import Report


class ReportAdmin(admin.ModelAdmin):
   
    list_display = (
        'id',
        'state',
        'pin',
        'color',
        'body_type',
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
                    'state',
                    'pin',
                    'color',
                    'body_type',
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

admin.site.register(Report, ReportAdmin)
