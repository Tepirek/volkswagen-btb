from django.db import models
from App.settings import AUTH_USER_MODEL


class Action(models.Model):

    name = models.CharField(
        verbose_name='Name',
        max_length=255,
        unique=True,
    )
    
    title = models.CharField(
        verbose_name='Title',
        max_length=255,
        null=True,
    ) 
    
    description = models.CharField(
        verbose_name='Description',
        max_length=255,
        null=True,
    ) 
    
    created_by = models.ForeignKey(
        verbose_name='Created by',
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE,
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

