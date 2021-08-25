from django.db import models
from ErrorType.models import ErrorType
from InclusionType.models import InclusionType
from ComponentType.models import ComponentType
from Report.models import Report
from App.settings import AUTH_USER_MODEL

STEPS = (
    'VBH/KTL',
    'PCV',
    'FL',
    'BC/CC',
)

class Point(models.Model):

    x = models.FloatField(
        verbose_name='X',
        null=False,
        blank=False,
    )

    y = models.FloatField(
        verbose_name='Y',
        null=False,
        blank=False,
    )

    error_type = models.ForeignKey(
        verbose_name='Error type',
        to=ErrorType,
        related_name='error_type',
        on_delete=models.CASCADE,
        null=True,
    )

    inclusion_type = models.ForeignKey(
        verbose_name='Inclusion type',
        to=InclusionType,
        related_name='inclusion_type',
        on_delete=models.CASCADE,
        null=True,
    )

    component_type = models.ForeignKey(
        verbose_name='Component type',
        to=ComponentType,
        related_name='component_type',
        on_delete=models.CASCADE,
        null=True,
    )

    report = models.ForeignKey(
        verbose_name='Report',
        to=Report,
        related_name='report',    
        on_delete=models.CASCADE,
        null=True,
    )

    stage = models.IntegerField(
        verbose_name='Stage',
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

