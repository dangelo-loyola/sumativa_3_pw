# Generated by Django 5.0.3 on 2024-04-30 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0012_alter_item_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='valor',
        ),
    ]