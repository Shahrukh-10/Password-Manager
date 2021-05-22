from django.shortcuts import HttpResponse, redirect, render
from django.conf import settings
from django.contrib.auth.hashers import make_password , check_password
from mainapp.encryption_util import *
from mainapp.models import Account, Password
import datetime
from django.http import request
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")
 


def handleLogin(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password'] 
        obj = Account.objects.get(email=email)
        request.session['email']=obj.email
        context= {
            "username" : obj.username
        }
        checkPassword = check_password(password,obj.mainpass)
        if checkPassword:
            messages.success(request, "Login Successful.")
            return render(request,'login.html',context)
        else:
            return redirect('/error')
    else:
        return render(request,"error.html")
    
def error(request):
    return render(request,"error.html")

def handleSignup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password'] 
        password = make_password(password)
        print(username , email ,password)

        a = Account(username=username,email=email,mainpass=password)
        a.save()
        messages.success(request,"Successfully registerered.")
        return render(request,"index.html")
    else:
        return render(request,"error.html")

def password(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        email=encrypt(email)
        password=encrypt(password)
        obj= Account.objects.get(email=request.session['email'])
        print(obj)
        passwordEntry = Password(userinfo=obj, email=email,password=password)
        passwordEntry.save()
        return HttpResponse("Saved")
    else:
        return render(request,"login.html")

        
def showPassword(request):
    obj= Account.objects.get(email=request.session['email'])
    date = datetime.datetime.now().strftime('%H:%M:%S')
    passwords = Password.objects.all().filter(userinfo=obj)
    print(passwords)
    for password in passwords:
        password.email = decrypt(password.email)
        password.password = decrypt(password.password)
    
    context = {"passwords":passwords,"username":obj.username,"date":date}
    return render(request,"passwords.html",context)