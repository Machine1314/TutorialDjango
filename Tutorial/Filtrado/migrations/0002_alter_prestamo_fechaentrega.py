# Generated by Django 4.0.1 on 2022-01-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filtrado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fechaEntrega',
            field=models.DateField(null=True, verbose_name='Fecha Entrega'),
        ),
    ]
