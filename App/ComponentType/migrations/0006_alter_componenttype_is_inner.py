# Generated by Django 3.2.6 on 2021-08-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComponentType', '0005_componenttype_is_inner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componenttype',
            name='is_inner',
            field=models.BooleanField(choices=[(0, 'inside'), (1, 'outside')], null=True, verbose_name='Is inner'),
        ),
    ]
