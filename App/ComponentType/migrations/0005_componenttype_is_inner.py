# Generated by Django 3.2.6 on 2021-08-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComponentType', '0004_componenttype_body_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='componenttype',
            name='is_inner',
            field=models.SmallIntegerField(choices=[(0, 'inside'), (1, 'outside')], max_length=255, null=True, verbose_name='Is inner'),
        ),
    ]
