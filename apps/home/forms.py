# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import forms
# Created by Tarun

class SearchForm(forms.Form):
    fromLocation=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "from",
                "class": "form-control"
            }
        ))
    toLocation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "to",
                "class": "form-control"
            }
        ))



