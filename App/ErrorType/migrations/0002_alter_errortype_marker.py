# Generated by Django 3.2.6 on 2021-08-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ErrorType', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errortype',
            name='marker',
            field=models.ImageField(upload_to='points/', verbose_name='Marker'),
        ),
    ]