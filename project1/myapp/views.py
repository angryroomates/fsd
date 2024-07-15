from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def datefunction(request):
    now = datetime.now()
    html="<html><body>This is current date and time %s.</body></html>"%now
    return HttpResponse(html)