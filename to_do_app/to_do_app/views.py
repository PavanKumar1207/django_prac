from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from . import models
from .models import TODOO
from django.contrib.auth import authenticate,login,logout
def signup(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        print(fnm,email,pwd)
        my_user=User.objects.create_user(fnm,email,pwd)
        return redirect('/loginn')

    return render(request,'signup.html')
def loginn(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr:
            login(request,userr)
            return redirect('todopage')
        else:
            return redirect('loginn')
    return render(request,'login.html')