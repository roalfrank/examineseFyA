# Generated by Django 4.0.1 on 2022-02-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_respuestas'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuestionario_usuario',
            name='completado',
            field=models.BooleanField(default=False),
        ),
    ]
