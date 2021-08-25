# Generated by Django 3.2.6 on 2021-08-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BodyType', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodytype',
            name='blueprint_inside',
            field=models.ImageField(null=True, upload_to='blueprints/', verbose_name='Blueprint inside'),
        ),
        migrations.AddField(
            model_name='bodytype',
            name='blueprint_outside',
            field=models.ImageField(null=True, upload_to='blueprints/', verbose_name='Blueprint outside'),
        ),
    ]
