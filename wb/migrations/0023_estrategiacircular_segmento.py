# Generated by Django 4.1.4 on 2023-01-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0022_remove_boaspraticas_estrategiacircular_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstrategiaCircular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrategiacircular', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmento', models.CharField(max_length=200)),
            ],
        ),
    ]
