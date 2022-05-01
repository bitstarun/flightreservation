# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    path('getsearch', views.getsearch, name="search"),
    path('getflightdetails', views.getflightdetails, name="flightdetails"),
    path('getseatdetails', views.getseatdetails, name="seatdetails"),
    path('bookticket', views.bookticket, name="bookticket"),
    path('index.html', views.index, name='home'),

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
