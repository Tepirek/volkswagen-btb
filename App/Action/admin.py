from django.contrib import admin
from .models import Action


class ActionAdmin(admin.ModelAdmin):
   
    list_display = (
        'id',
        'name',
        'title',
        'description',
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
                    'title',
                    'description',
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
        'title',
        'description',
        'created_by',
        'created_at',
        'updated_at',
    )

    ordering = (
        'id',
    )

admin.site.register(Action, ActionAdmin)
