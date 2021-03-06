# Generated by Django 4.0.6 on 2022-07-11 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('boat_type', models.CharField(choices=[('M', 'Motorboat'), ('C', 'Cabin cruiser'), ('D', 'Dinghy'), ('K', 'Keel boat')], max_length=32)),
                ('location', models.CharField(max_length=64)),
                ('has_motor', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BoatDamages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage', models.CharField(max_length=128)),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boats.boat')),
            ],
        ),
    ]
