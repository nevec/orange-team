from django.shortcuts import render

from django.http import HttpResponse

def index(req):
	return HttpResponse(render(req, 'accounts/index.html', {}))

def map(req):
	return HttpResponse(render(req, 'accounts/map.html', {}))

def test(req):
	return HttpResponse(render(req, 'accounts/test.html', {}))

def login(req):
	return HttpResponse(render(req, 'accounts/login.html'), {})

def register(req):
	return HttpResponse(render(req, 'accounts/register.html'), {})
# Create your views here.
