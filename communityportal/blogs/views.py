from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate
from .models import Posts
from .forms import PostForm
# Create your views here.
def home(request):
    posts = Posts.objects.all()
    return render(request,'blog/home.html',{'posts':posts})
def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')
def user_logout(request):
    logout(request)
    return redirect('contact')
def user_login(request):
    
        if request.method=='POST':
            uname = request.POST['userName']
            password=request.POST['passWord']
            if (uname=='' or password==''):
                messages.info(request,'Please fill all fields')
                return redirect('user_login')
            user=authenticate(username=uname,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Invalid username password')
            return redirect('user_login')
        else:
            return render(request,'blog/login.html')
    
def signup(request):
    if request.method=='POST':
        fname=request.POST['firstName']
        lname=request.POST['lastName']
        uname=request.POST['userName']
        email=request.POST['email']
        p1=request.POST['password1']
        p2=request.POST['password2']
        if (fname=='' or lname=='' or uname=='' or email =='' or p1 =='') :
            messages.info(request,'Please fill all the fields')
            return redirect('signup')
        if(p1==p2):
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Useername exist')
                return redirect('signup')
            else:
                 if User.objects.filter(email=email).exists():
                    messages.info(request,'email exist')
                    return redirect('signup')
                 else:
                    user= User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=p1)
                    user.save()
           #adding to author group
                    group=Group.objects.get(name='Author')
                    user.groups.add(group)
                    return redirect('user_login')
        else:
            messages.info(request,'password not matching')
            return redirect('signup')
            
    else:
        return render(request,'blog/signup.html')
def dashboard(request):
    if request.user.is_authenticated:
        posts=Posts.objects.all()
        return render(request,'blog/dashboard.html',{'posts':posts})
    else:
       return redirect('user_login')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['description']
                pst=Posts(title=title,description=desc)
                pst.save()
                form=PostForm()
                message="Succesfully added"
        else:
            form = PostForm()
            message=" "
        return render(request,'blog/add_post.html',{'form':form,'message':message})
    else:
        return redirect('user_login')


def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = Posts.objects.get(pk=id)
            form  = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Posts.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form,'pi':id})
    
    else:
        return redirect('user_login')

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi= Posts.objects.get(pk=id)
            pi.delete()
            return redirect('dashboard')
    else:
        return redirect('user_login')