from django.db import models
from App.settings import AUTH_USER_MODEL


class Summary(models.Model):

    TYPES = (
        ('weekly', 'weekly'),
        ('monthly', 'monthly'),
        ('yearly', 'yearly'),
        ('custom', 'custom'),
    )

    file = models.FileField(
        verbose_name='File',
        upload_to='summaries/'
    )

    type = models.CharField(
        verbose_name='Type',
        max_length=255,
        choices=TYPES, 
    )

    date_start = models.DateTimeField(
        verbose_name='Date start',
    )

    date_end = models.DateTimeField(
        verbose_name='Date end',
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