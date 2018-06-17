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

def login(req):
	return HttpResponse(render(req, 'accounts/login.html'), {})

def register(req):
	return HttpResponse(render(req, 'accounts/register.html'), {})
# Create your views here.
