from django.db import models
from App.settings import AUTH_USER_MODEL


class BodyType(models.Model):
    
    name = models.CharField(
        verbose_name='Name',
        max_length=255,
        null=False,
        blank=False,
    )

    blueprint_inside = models.ImageField(
        verbose_name='Blueprint inside',
        upload_to='blueprints/',
        null=True,
    )

    blueprint_outside = models.ImageField(
        verbose_name='Blueprint outside',
        upload_to='blueprints/',
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
