import random

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers.address.en_IN import Provider
from faker_airtravel import AirTravelProvider
from apps.home.models import ROUTEDETAILS, FLIGHTDETAILS, SEATDETAILS, TICKET
import datetime

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(["nl_NL"])
        fake.add_provider(Provider)
        fake.add_provider(faker.providers.date_time.Provider)
        fake.add_provider(AirTravelProvider)
        print("Running data insertion tool")
        # routeid = models.AutoField(primary_key=True)
        # departureairportname = models.CharField("departureairportname", max_length=50)
        # departurecity = models.CharField("departurecity", max_length=30)
        # departurestate = models.CharField("departurestate", max_length=30)
        # destinationeairportname = models.CharField("destinationairportname", max_length=50)
        # destinationcity = models.CharField("destinationcity", max_length=30)
        # destinationstate = models.CharField("destinationstate", max_length=30)
        # departuretime = models.DateTimeField("departuretime", max_length=30)
        # destinationtime = models.DateTimeField("destinationtime", max_length=30)

        # flightid = models.AutoField(primary_key=True)
        # routeid = models.ForeignKey(ROUTEDETAILS, verbose_name='routeid', on_delete=models.CASCADE,)
        # airline = models.CharField("airline", max_length=30)
        # flightname = models.CharField("flightname", max_length=30)
        # flighttype = models.CharField("flighttype", max_length=15)
        # flightcapacity = models.IntegerField("flightcapacity", null=True, blank=True)
        fID = 10000
        sID = 30000 
        tID = 70000
        for i in range(1000, 1050):
            # print(i, fake.,fakefake.city_name() )
            flt = fake.flight()
            rid = i
            origin = flt['origin']
            dest = flt['destination']
            departureairportname = origin['airport']
            departurecity = origin['city']
            departurestate = origin['state']
            departurecountry = origin['country']
            destinationeairportname = dest['airport']
            destinationcity = dest['city']
            destinationstate = dest['state']
            destinationcountry = dest['country']
            departuretime = fake.date_time_this_month()
            destinationtime = departuretime + datetime.timedelta(hours=12)
            airline = flt['airline']
            price = flt['price']
            flighttype = flt['stops']

            rd = ROUTEDETAILS.objects.create(
                routeid=rid,
                departureairportname=departureairportname,
                departurecity=departurecity,
                departurestate=departurestate,
                departurecountry=departurecountry,
                destinationeairportname=destinationeairportname,
                destinationcity=destinationcity,
                destinationstate=destinationstate,
                destinationcountry=destinationcountry,
                departuretime=departuretime,
                destinationtime=destinationtime)

            fID = fID + i
            fc = fake.random_int(min=500, max=900)
            fDet = FLIGHTDETAILS.objects.create(
                flightid=fID,
                routeid=rd,
                airline=airline,
                flightname=fake.text()[0:8],
                flighttype = flighttype,
                flightcapacity = fc
            )
            sID = sID + i 
            tID = tID + i
            for j in range(fc):
                sDet = SEATDETAILS.objects.create(
                    seatid = sID + j,
                    flightid = fDet,
                    seatnumber = j,
                    seatclass = "Executive",
                    price = price
                )

                TICKET.objects.get_or_create(
                    ticketid = tID + j,
                    flightid = fDet,
                    seatid = sDet,
                    status = True,
                    bookingdate = None
                )
            # print(routeid, airline, departureairportname, departurecity, departurestate, departurecountry)
            # print(destinationeairportname, destinationcity, destinationstate, destinationcountry, departuretime, destinationtime)
            # print(airline, price)
        
        print("Data Inserted")