#from django.shortcuts import render
ifrom django.http import HttpResponse

# Create your views here.


def index(request):
	return HttpResponse("Welcome to LTI")
