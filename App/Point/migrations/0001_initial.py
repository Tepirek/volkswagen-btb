# Generated by Django 3.2.6 on 2021-08-09 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('InclusionType', '0001_initial'),
        ('ErrorType', '0001_initial'),
        ('ComponentType', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(verbose_name='X')),
                ('y', models.IntegerField(verbose_name='Y')),
                ('location', models.CharField(choices=[('inside', 'inside'), ('outside', 'outside')], max_length=255, verbose_name='Location')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('component_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='component_type', to='ComponentType.componenttype', verbose_name='Component type')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('error_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='error_type', to='ErrorType.errortype', verbose_name='Error type')),
                ('inclusion_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inclusion_type', to='InclusionType.inclusiontype', verbose_name='Inclusion type')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]