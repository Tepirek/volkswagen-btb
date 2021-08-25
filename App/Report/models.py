from django.db import models

from App.storage import OverwriteStorage
from Color.models import Color
from BodyType.models import BodyType
from App.settings import AUTH_USER_MODEL


class Report(models.Model):

    STATES = (
        ('pending', 'pending'),
        ('done', 'done'),
    )

    state = models.CharField(
        verbose_name='State',
        max_length=255,
        choices=STATES, 
        default='pending',
    )

    pin = models.CharField(
        verbose_name='PIN',
        max_length=255,
        null=False,
        blank=False,
    )

    color = models.ForeignKey(
        verbose_name='Color',
        to=Color,
        on_delete=models.CASCADE,
        null=True,
    )

    blueprint_inside = models.ImageField(
        verbose_name='Blueprint inside',
        upload_to='reports/',
        null=True,
        storage=OverwriteStorage()
    )

    blueprint_outside = models.ImageField(
        verbose_name='Blueprint outside',
        upload_to='reports/',
        null=True,
        storage=OverwriteStorage()
    )

    body_type = models.ForeignKey(
        verbose_name='Body type',
        to=BodyType,
        on_delete=models.CASCADE,
        null=True,
    )

    sent_at = models.DateTimeField(
        verbose_name='Sent at',
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
        ordering = ['created_at']
