# Generated by Django 3.2.6 on 2021-08-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComponentType', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componenttype',
            name='image',
            field=models.ImageField(upload_to='storage/components/', verbose_name='Image'),
        ),
    ]