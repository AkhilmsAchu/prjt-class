from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("<h2>hello world</h2>")
def profile(request):
	return HttpResponse("<h2>hai</h2>")