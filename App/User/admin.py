from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = (
        'id',
        'worker_id',
        'email',
        'avatar',
        'first_name',
        'last_name',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'last_login',
    )

    list_editable = (
        'first_name',
        'last_name',
        'is_superuser',
        'is_staff',
        'is_active',
    )

    list_filter = (
        
    )

    fieldsets = (
        (
            'Base data', {
                'fields': (
                    'worker_id',
                    'email',
                ),
            },
        ),
        (
            'Security', {
                'fields': (
                    'password',
                ),
            },
        ),
        (
            'Permissions', {
                'fields': (
                    'is_superuser',
                    'is_staff',
                    'is_active',
                    'groups',
                ),
            },
        ),
    )

    search_fields = (
        'worker_id',
        'email',
        'first_name',
        'last_name',
    )
    
    ordering = (
        'id',
    )

admin.site.register(User, UserAdmin)
