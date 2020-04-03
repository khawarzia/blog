from django.shortcuts import render
from .models import *
from loginreg.models import *
from loginreg.forms import *
from .forms import *

def getprofilepic(request):
    try:
        a = profile.objects.get(user=request.user)
        return a.profile_pic.url
    except:
        return '/static/images/dog.jpg'

def profilepage(request,usr):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        if usr != request.user.username:
            return redirect('/')
    template = 'post/profile.html'
    context = {}
    form = profilepicform(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        a = profile.objects.last()
        a.user = request.user
        a.save()
        objs = profile.objects.filter(user=request.user)
        if len(objs) > 1:
            for i in objs:
                if i != a:
                    i.delete()
    form = profilepicform()
    form2 = pictureform()
    context['form'] = form
    context['form2'] = form2
    context['profilephoto'] = getprofilepic(request)
    context['posts'] = post.objects.filter(user=request.user)
    return render(request,template,context)

def newpost(request):
    form = pictureform(request.POST or None,request.FILES or None)
    a = request.POST['title']
    b = request.POST['content']
    if form.is_valid():
        form.save()
        obj = post.objects.last()
    else:
        obj = post()
    obj.user = request.user
    obj.title = a
    obj.text = b
    obj.save()
    return redirect('/')