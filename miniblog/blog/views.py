from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post,About
# Create your views here.

def home(request):
    Posts=Post.objects.all()
    return render(request,'blog/home.html',{'Posts':Posts})

def navbar(request):
    return render(request, 'blog/navbar.html')

def about(request):
    about=About.objects.all()
    return render(request, 'blog/about.html',{'about':about})

def contact(request):
    return render(request, 'blog/contact.html')

def addpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                pst.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            form=PostForm()
        return render(request, 'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request, 'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def dashboard(request):
    if request.user.is_authenticated:
        Posts=Post.objects.all()
        return render(request, 'blog/dashboard.html',{'Posts':Posts})
    else:
        return HttpResponseRedirect('/login/')
        
        

def user_signup(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!!! You are Signed Up ')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'{{user}} Logged in Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')