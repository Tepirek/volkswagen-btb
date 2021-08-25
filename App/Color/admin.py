from django.contrib import admin
from .models import Color


class ColorAdmin(admin.ModelAdmin):
  
    list_display = (
        'id',
        'name',
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
                'fields': (
                    'name',
                ),
            },
        ),
        (
            'Creation', {
                'fields': (
                    'created_by',
                ),
            },
        ),
    )

    search_fields = (
        'name',
    )

    ordering = (
        'id',
    )

admin.site.register(Color, ColorAdmin)