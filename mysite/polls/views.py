from django.shortcuts import render

from django.http import HttpResponse

def in(request):
	return HttpResponse("Hello, world. You're at the polls index.")
