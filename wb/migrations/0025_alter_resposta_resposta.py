# Generated by Django 4.1.4 on 2023-01-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0024_boaspraticas_estrategiacircular_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='resposta',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
