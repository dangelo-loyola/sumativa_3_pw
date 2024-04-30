# Generated by Django 5.0.3 on 2024-04-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_item_delete_juegops4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
