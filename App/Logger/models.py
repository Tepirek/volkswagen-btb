from django.db import models
from Action.models import Action
from App.settings import AUTH_USER_MODEL


class Logger(models.Model):
    
    action = models.ForeignKey(
        verbose_name='Action',
        to=Action,
        related_name='action',
        on_delete=models.CASCADE,
        null=True,
    )

    created_by = models.ForeignKey(
        verbose_name='Created by',
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    type = models.CharField(
        verbose_name='Type',
        max_length=255,
        null=True
    )

    reference = models.IntegerField(
        verbose_name='Reference ID',
        default=0,
    )

    is_visible = models.BooleanField(
        verbose_name='Is visible',
        default=True
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
        ordering = ['-created_at']



