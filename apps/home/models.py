# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ROUTEDETAILS(models.Model):
    routeid = models.AutoField(primary_key=True)
    departureairportname = models.CharField("departureairportname", max_length=50)
    departurecity = models.CharField("departurecity", max_length=30)
    departurestate = models.CharField("departurestate", max_length=30)
    departurecountry = models.CharField("departurecountry", max_length=30)
    destinationeairportname = models.CharField("destinationairportname", max_length=50)
    destinationcity = models.CharField("destinationcity", max_length=30)
    destinationstate = models.CharField("destinationstate", max_length=30)
    destinationcountry = models.CharField("destinationcountry", max_length=30)
    departuretime = models.DateTimeField("departuretime", max_length=30)
    destinationtime = models.DateTimeField("destinationtime", max_length=30)
    
class FLIGHTDETAILS(models.Model):
    flightid = models.AutoField(primary_key=True)
    routeid = models.ForeignKey(ROUTEDETAILS, verbose_name='routeid', on_delete=models.CASCADE,)
    airline = models.CharField("airline", max_length=30)
    flightname = models.CharField("flightname", max_length=30)
    flighttype = models.CharField("flighttype", max_length=15)
    flightcapacity = models.IntegerField("flightcapacity", null=True, blank=True)

class SEATDETAILS(models.Model):
    seatid = models.AutoField(primary_key=True)
    flightid = models.ForeignKey(FLIGHTDETAILS, verbose_name='flightid', on_delete=models.CASCADE,)
    seatnumber = models.IntegerField("seatnumber", null=True, blank=True)
    seatclass = models.CharField("seatclass", max_length=15)
    price = models.DecimalField("price",max_digits=10, decimal_places=2)

class TICKET(models.Model):
    ticketid = models.AutoField(primary_key=True)
    flightid = models.ForeignKey(FLIGHTDETAILS, verbose_name='flightid', on_delete=models.CASCADE,)
    seatid = models.ForeignKey(SEATDETAILS, verbose_name='seatid', on_delete=models.CASCADE,)
    status = models.BooleanField("status")
    bookingdate = models.DateTimeField("bookingdate", max_length=30, null=True)
    username = models.CharField("username", max_length=30, null=True)

