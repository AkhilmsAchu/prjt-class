from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import property as promodel
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
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
		
		if User.objects.filter(username=un).exists():
			return render(request,'register.html',{'msg':"username already taken"})
		else:
			userob=User.objects.create_user(username=un,password=pwd,first_name=fn,last_name=ln,email=email)
			userob.save()
			print("user created")
			return redirect('/')
	
		
	else:
		return render(request,'register.html')

def login(request):

	if request.method=='POST':
		un=request.POST['username']
		pwd=request.POST['password']
		userob=auth.authenticate(username=un,password=pwd)
		if userob is not None:
			auth.login(request, userob)
			return redirect("/")
		else:
			return render(request,'login.html',{'msg':"username or password doesn't exist"})


	else:
		return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect("/")

def editprofile(request):
	if request.method=='POST':
		fn=request.POST['fname']
		ln=request.POST['lname']
		pwd=request.POST['password']
		userob=request.user
		userob.first_name=fn
		userob.last_name=ln
		userob.set_password(pwd)
		userob.save()
		return redirect("/")
	else:
		return render(request,'editprofile.html')

def singlepro(request):
	var=request.GET['id']
	try:
		pro=promodel.objects.get(id=var)
	except Exception as e:
		print(e)
		return redirect('/')
	print(pro)
	return render(request,'property-single.html',{'property':pro})

@login_required(login_url='login')
def deletepro(request):
	var=request.GET['id']
	try:
		pro=promodel.objects.get(id=var)
		pro.delete()
	except Exception as e:
		print(e)
		return redirect('/')
	return redirect('property')

def editpro(request):
	if request.method=='POST':
		var=request.POST['id']
		newname=request.POST['name']
		newprice=request.POST['price']
		pro=promodel.objects.get(id=var)
		pro.name=newname
		pro.price=newprice
		pro.save()
		return redirect("property")
	else:
		var=request.GET['id']
		pro=promodel.objects.get(id=var)
		return render(request,'editpro.html',{'property':pro})