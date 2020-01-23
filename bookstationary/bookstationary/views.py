#I have created this page - iqra
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')




def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    puntuations = ''':()-[]{};!'"\,<>./?@*_~'''
    analyzed = ""
    for char in djtext:
        if char not in puntuations:
            analyzed = analyzed + char  
    params = {'purpose':'Removed Puntuatres','analyzed_text': analyzed}
    return render(request,'analyze.html',params)
    
    