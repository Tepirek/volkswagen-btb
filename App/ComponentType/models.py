from django.db import models
from App.settings import AUTH_USER_MODEL
from BodyType.models import BodyType

LOCATIONS = (
        (1, 'inside'),
        (0, 'outside'),
    )

class ComponentType(models.Model):
    
    name = models.CharField(
        verbose_name='Name',
        max_length=255,
    )

    image = models.ImageField(
        verbose_name='Image',
        upload_to='components/'
    )
    
    body_type = models.ForeignKey(
        verbose_name='Body type',
        to=BodyType,
        on_delete=models.CASCADE,
        null=True,
    )

    is_inner = models.BooleanField(
        verbose_name='Is inner',
        choices=LOCATIONS,
        null=True,
    )

    created_by = models.ForeignKey(
        verbose_name='Created by',
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['id']