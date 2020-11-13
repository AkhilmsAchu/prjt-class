from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import property as promodel
from django.contrib.auth.models import User
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

def register(request):
	if request.method=='POST':
		fn=request.POST['fname']
		ln=request.POST['lname']
		email=request.POST['email']
		un=request.POST['username']
		pwd=request.POST['password']
		
		userob=User.objects.create_user(username=un,password=pwd,first_name=fn,last_name=ln,email=email)
		userob.save()
		print("user created")
		return redirect('/')
	
		
	else:
		return render(request,'register.html')