# Generated by Django 3.2.6 on 2022-04-27 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FLIGHTDETAILS',
            fields=[
                ('flightid', models.AutoField(primary_key=True, serialize=False)),
                ('airline', models.CharField(max_length=30, verbose_name='airline')),
                ('flightname', models.CharField(max_length=30, verbose_name='flightname')),
                ('flighttype', models.CharField(max_length=15, verbose_name='flighttype')),
                ('flightcapacity', models.IntegerField(blank=True, null=True, verbose_name='flightcapacity')),
            ],
        ),
        migrations.CreateModel(
            name='ROUTEDETAILS',
            fields=[
                ('routeid', models.AutoField(primary_key=True, serialize=False)),
                ('departureairportname', models.CharField(max_length=50, verbose_name='departureairportname')),
                ('departurecity', models.CharField(max_length=30, verbose_name='departurecity')),
                ('departurestate', models.CharField(max_length=30, verbose_name='departurestate')),
                ('departurecountry', models.CharField(max_length=30, verbose_name='departurecountry')),
                ('destinationeairportname', models.CharField(max_length=50, verbose_name='destinationairportname')),
                ('destinationcity', models.CharField(max_length=30, verbose_name='destinationcity')),
                ('destinationstate', models.CharField(max_length=30, verbose_name='destinationstate')),
                ('destinationcountry', models.CharField(max_length=30, verbose_name='destinationcountry')),
                ('departuretime', models.DateTimeField(max_length=30, verbose_name='departuretime')),
                ('destinationtime', models.DateTimeField(max_length=30, verbose_name='destinationtime')),
            ],
        ),
        migrations.CreateModel(
            name='SEATDETAILS',
            fields=[
                ('seatid', models.AutoField(primary_key=True, serialize=False)),
                ('seatnumber', models.IntegerField(blank=True, null=True, verbose_name='seatnumber')),
                ('seatclass', models.CharField(max_length=15, verbose_name='seatclass')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('flightid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.flightdetails', verbose_name='flightid')),
            ],
        ),
        migrations.CreateModel(
            name='TICKET',
            fields=[
                ('ticketid', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(verbose_name='status')),
                ('bookingdate', models.DateTimeField(max_length=30, null=True, verbose_name='bookingdate')),
                ('flightid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.flightdetails', verbose_name='flightid')),
                ('seatid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.seatdetails', verbose_name='seatid')),
            ],
        ),
        migrations.AddField(
            model_name='flightdetails',
            name='routeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.routedetails', verbose_name='routeid'),
        ),
    ]