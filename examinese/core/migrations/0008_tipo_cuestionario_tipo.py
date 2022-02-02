# Generated by Django 4.0.1 on 2022-02-02 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cuestionario_usuario_completado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
            options={
                'verbose_name_plural': 'Tipo',
            },
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='tipo',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.tipo', verbose_name='Tipo Cuestionario'),
        ),
    ]
