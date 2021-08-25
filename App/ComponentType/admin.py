from django.contrib import admin
from .models import ComponentType


class ComponentTypeAdmin(admin.ModelAdmin):
   
    list_display = (
        'id',
        'name',
        'image',
        'body_type',
        'is_inner',
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
                    'image',
                ],
            },
        ),
        (
            'Locus', {
                'fields': [
                    'body_type',
                    'is_inner',
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

admin.site.register(ComponentType, ComponentTypeAdmin)
