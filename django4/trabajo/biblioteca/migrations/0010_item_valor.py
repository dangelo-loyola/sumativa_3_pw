# Generated by Django 5.0.3 on 2024-04-30 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0009_delete_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='valor',
            field=models.IntegerField(default=0),
        ),
    ]
