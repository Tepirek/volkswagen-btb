# Generated by Django 3.2.6 on 2021-08-21 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='summaries/', verbose_name='File')),
                ('type', models.CharField(choices=[('weekly', 'weekly'), ('monthly', 'monthly'), ('yearly', 'yearly'), ('custom', 'custom')], max_length=255, verbose_name='Type')),
                ('date_start', models.DateTimeField(auto_now_add=True, verbose_name='Date start')),
                ('date_end', models.DateTimeField(auto_now_add=True, verbose_name='Date end')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
