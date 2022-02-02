# Generated by Django 4.0.1 on 2022-02-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_tipo_cuestionario_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo',
            name='descripcion',
            field=models.CharField(default='lolo', max_length=500, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nombre',
            field=models.CharField(max_length=500, verbose_name='nombre'),
        ),
    ]
