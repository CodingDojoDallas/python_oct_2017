# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponse

def index(req):
    resp = "This is the home page"
    return HttpResponse(resp)
