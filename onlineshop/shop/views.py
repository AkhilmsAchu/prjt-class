from django.shortcuts import render
from django.http import HttpResponse
from .models import property as promodel
# Create your views here.
def home(request):
	return render(request,'index.html',{'name':'akhil','age':'12'})
def profile(request):
	return HttpResponse("<h2>hai</h2>")

def add(request):
	var1=int(request.POST['num1'])
	var2=int(request.POST['num2'])
	print(type(var1))
	result=var1+var2
	return render(request,'result.html',{'result':result})
def about(request):
	return render(request,'about.html')
def property(request):
	pro=promodel.objects.all()
	return render(request,'property-grid.html',{'properties':pro})