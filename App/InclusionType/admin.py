from django.contrib import admin
from .models import InclusionType


class InclusionTypeAdmin(admin.ModelAdmin):
   
    list_display = (
        'id',
        'name',
        'marker',
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
                    'name',
                    'marker',
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

admin.site.register(InclusionType, InclusionTypeAdmin)
