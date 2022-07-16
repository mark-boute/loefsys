# Generated by Django 4.0.6 on 2022-07-11 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0001_initial'),
        ('users', '0002_remove_user_id_alter_user_relation_number'),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoatReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motor_time', models.TimeField(blank=True, null=True)),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boats.boat')),
                ('skipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolved', models.BooleanField()),
                ('repair_costs', models.IntegerField()),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Boat',
        ),
        migrations.AddField(
            model_name='reservation',
            name='fine',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='damage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.damage'),
        ),
    ]