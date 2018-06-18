from django.shortcuts import render

from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
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

def get_log_pass(req):
	dict = req.POST
	user = authenticate(req, username=dict['login'], password=dict['pass'])
	#login(req,user)
	return HttpResponseRedirect('/')

def get_reg(req):
	dict = req.POST
	user = User.objects.create_user(dict['login'],dict['email'],dict['password'])
	user.is_active = False
	#user.first_name = dict['firstname']
	#user.last_name = dict['lastname']
	user.save()
	return HttpResponseRedirect('/')	
# Create your views here.
