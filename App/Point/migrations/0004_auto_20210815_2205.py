# Generated by Django 3.2.6 on 2021-08-15 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Point', '0003_remove_point_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='stage',
            field=models.IntegerField(null=True, verbose_name='Stage'),
        ),
        migrations.AlterField(
            model_name='point',
            name='x',
            field=models.FloatField(verbose_name='X'),
        ),
        migrations.AlterField(
            model_name='point',
            name='y',
            field=models.FloatField(verbose_name='Y'),
        ),
    ]
