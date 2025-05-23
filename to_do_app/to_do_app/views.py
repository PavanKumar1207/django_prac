from django.shortcuts import render,redirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User 
from . import models
from .models import TODOO
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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
@login_required(login_url='/loginn')
def todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.TODOO(title=title,user=request.user)
        obj.save()
        res=models.TODOO.objects.filter(user=request.user).order_by('date')
        return redirect('/todopage',{'res':res})
    res=models.TODOO.objects.filter(user=request.user).order_by('date')
    return render(request,'todo.html',{'res':res})
@login_required(login_url='/loginn')
def edit_todo(request,srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODOO.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todopage')

    obj = models.TODOO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})
def signout(request):
    logout(request)
    return redirect('/loginn')
def delete_todo(request,srno):
    todo = models.TODOO.objects.get(srno=srno)
    todo.delete()
    return redirect('/todopage')
def mark_completed(request, srno):
    todo = get_object_or_404(TODOO, srno=srno)
    todo.status = True
    todo.save()
    return redirect('/todopage')