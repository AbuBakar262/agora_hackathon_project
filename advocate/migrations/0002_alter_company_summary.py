# Generated by Django 4.1.2 on 2022-10-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='summary'),
        ),
    ]
