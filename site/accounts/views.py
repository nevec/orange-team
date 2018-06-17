from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Place

def index(req):
	return HttpResponse(render(req, 'accounts/index.html', {}))

def map(req):
	return HttpResponse(render(req, 'accounts/map.html', {}))

def test(req):
	return HttpResponse(render(req, 'accounts/test.html', {}))

def getPlaces(req):

	resp = {}

	for o in Place.objects.all():
		resp[o.place_name] = {'lat' : o.lat, 'lon': o.lon}

	return JsonResponse(resp)

# Create your views here.
