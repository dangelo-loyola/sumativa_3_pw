# Generated by Django 5.0.3 on 2024-04-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_cliente_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='password',
        ),
        migrations.AddField(
            model_name='cliente',
            name='contraseña',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_completo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_usuario',
            field=models.CharField(max_length=50),
        ),
    ]
