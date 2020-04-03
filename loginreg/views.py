from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from loginreg.models import *

def home(request):
    if request.user.is_authenticated:
        return redirect('/profile/'+request.user.username)
    return render(request,'base.html')

def login(request):
    template = 'login/login.html'
    context = {}
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['pass']
        try:
            c = User.objects.get(email=a)
        except:
            context['message'] = 'No such user exists!'
            return render(request,template,context)
        if c.check_password(b):
            auth.login(request,c)
            return redirect('/')
        else:
            context['message'] = 'The password you entered was wrong!'
            return render(request,template,context)
    return render(request,template,context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    template = 'login/signup.html'
    context = {}
    if request.method == 'POST':
        a = request.POST['fname']
        b = request.POST['lname']
        c = request.POST['email']
        d = request.POST['pass1']
        e = request.POST['pass2']
        if d != e:
            context['message'] = 'The entered passwords did not match!'
            return render(request,template,context)
        if len(d) < 8:
            context['message'] = 'Password should be at least 8 character!'
            return render(request,template,context)
        try:
            f = User.objects.get(email=c)
            context['message'] = 'The entered email already belongs to an account!'
            return render(request,template,context)
        except:
            pass
        obj = User()
        obj.first_name = a
        obj.last_name = b
        obj.email = c
        obj.username = c.split('@')[0]
        obj.save()
        obj.set_password(d)
        obj.save()
        auth.login(request,obj)
        return redirect('/')
    return render(request,template,context)