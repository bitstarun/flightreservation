# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import ROUTEDETAILS as rd
from apps.home.models import FLIGHTDETAILS as fd
from apps.home.models import SEATDETAILS as sd
from apps.home.models import TICKET as ticket
from datetime import datetime

# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    
    fromLocation = request.POST.get("fromcity", None)
    toLocation = request.POST.get("tocity", None)
    if (fromLocation is not None and toLocation is None):
        # context['fromcity'] = list(fromLocation)
        context['tocity'] = list(rd.objects.filter(departurecity=fromLocation).values_list('destinationcity', flat=True).distinct())
        return (HttpResponse(context['tocity']))
    else:
        context['fromcity'] = list(rd.objects.order_by().values_list('departurecity', flat=True).distinct())
        context['tocity'] = list(rd.objects.order_by().values_list('destinationcity', flat=True).distinct())
        
    # context['toaddress'] = 
    html_template = loader.get_template('flight/index.html')
    return HttpResponse(html_template.render(context, request))

def getsearch(request):
    context = {'segment': 'routedetails'}
    fromLocation = request.POST.get("fromcity", None)
    toLocation = request.POST.get("tocity", None)
    records = rd.objects.filter(departurecity=fromLocation,destinationcity=toLocation)
    context["routedetails"] = records
    html_template = loader.get_template('flight/routedetails.html')
    return HttpResponse(html_template.render(context, request))

def getflightdetails(request):
    context = {'segment': 'flightdetails'}
    routeid = request.GET.get("routeid", None)
    if(routeid is not None):
        records = fd.objects.filter(routeid=routeid)
        context["flightdetails"] = records
        html_template = loader.get_template('flight/flightdetails.html')
        return HttpResponse(html_template.render(context, request))
    else:
        html_template = loader.get_template('flight/routedetails.html')
        return HttpResponse(html_template.render(context, request))

def getseatdetails(request):
    context = {'segment': 'seatdetails'}
    flightid = request.GET.get("flightid", None)
    if(flightid is not None):
        records = sd.objects.filter(flightid_id=flightid).filter(ticket__status=1)
        context["seatdetails"] = records
        html_template = loader.get_template('flight/seatdetails.html')
        return HttpResponse(html_template.render(context, request))
    else:
        html_template = loader.get_template('flight/routedetails.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def bookticket(request):
    context = {'segment': 'bookingdetails'}
    seatid = request.GET.get("seatid", None)
    if(seatid is not None):
        updaterecords = ticket.objects.get(seatid_id=seatid)
        updaterecords.bookingdate = datetime.now()
        updaterecords.status = 0
        updaterecords.username= request.user.username
        updaterecords.save(update_fields=['bookingdate', 'status', 'username'])
        records = ticket.objects.filter(seatid_id=seatid).prefetch_related()
        
        context['bookingdetails'] = records
    
    html_template = loader.get_template('flight/bookingdetails.html')
    return HttpResponse(html_template.render(context, request))

# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        if load_template == 'login':
            print("Login screen")    
            return HttpResponseRedirect(reverse('login'))
        context['segment'] = load_template

        html_template = loader.get_template('flight/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
