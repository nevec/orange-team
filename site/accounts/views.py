from django.shortcuts import render

from django.http import HttpResponse

def index(req):
	return HttpResponse(render(req, 'accounts/index.html', {}))

def map(req):
	return HttpResponse(render(req, 'accounts/map.html', {}))

# Create your views here.
