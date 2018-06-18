from django.shortcuts import render

from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
import django.contrib.auth as auth
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

def loginp(req):
	return HttpResponse(render(req, 'accounts/login.html'), {})

def register(req):
	return HttpResponse(render(req, 'accounts/register.html'), {})

def get_log_pass(req):
	dict = req.POST

	user = authenticate(req, username=dict['login'], password=dict['pass'])
	if user is not None:
		login(req,user)
	return HttpResponseRedirect('/success/')

def get_reg(req):
	dict = req.POST
	user = User.objects.create_user(dict['login'],dict['email'],dict['password'])
	user.is_active = False
	flag = 1
	for i in dict:
		if (i == None):
			flag = 0
	if (flag == 1):			
		user.save()
		return HttpResponseRedirect('/')	
	else:
		return HttpResponseRedirect('/register/')	
# Create your views here.

def test2(req):
	return HttpResponse(render(req, 'accounts/test2.html'), {})

def success(req):
	return HttpResponse(render(req, 'accounts/success.html'), {})

def logout(req):
	auth.logout(req)
	return HttpResponseRedirect('/')

def test_res(req):
	return HttpResponse(render(req, 'accounts/test_res.html'), {})