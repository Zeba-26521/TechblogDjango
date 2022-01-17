from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm,LoginForm, AddpostForm
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from .models import Blogpost
from django.contrib.auth.models import Group


# home
def home(request):
    posts=Blogpost.objects.all()
    return render(request,'myblog/home.html',{'posts':posts})

# about
def about(request):
    return render(request,'myblog/about.html')

# contact
def contact(request):
    return render(request,'myblog/contact.html')

# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts=Blogpost.objects.all()
        fullname=request.user.get_full_name()
        grps=request.user.groups.all()
        userid=request.user.id

        return render(request,'myblog/dashboard.html',{'posts':posts,'fullname':fullname,'grps':grps,'userid':userid})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#Signup
def user_signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congrats!! You have sucessfully Signed up')
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form=SignupForm()
    
    return render(request,'myblog/signup.html', {'form':form})

# Login
def user_login(request):
    if not request.user.is_authenticated:     
        if request.method == 'POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'you have logged in successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=LoginForm()
        return render(request,'myblog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

# Add post
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=AddpostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                des=form.cleaned_data['desc']
                autho=form.cleaned_data['autho']
                pst=Blogpost(title=title,desc=des,autho=autho)
                pst.save()
                messages.success(request,'Congrats!! You have sucessfully added post ')

                form=AddpostForm()

        else:
            form=AddpostForm()       
        return render(request,'myblog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

# Edit post
def edit_post(request,id):
    if request.user.is_authenticated:
        userid=request.user.id
        fullname=request.user.get_full_name()      
        grp=request.user.groups.all()  
        if request.method=='POST':
            pi=Blogpost.objects.get(pk=id)
            pid=pi.autho.id
            form=AddpostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
            messages.success(request,'Congrats!! You have sucessfully edited post ')

        else:
            pi=Blogpost.objects.get(pk=id)
            form=AddpostForm(instance=pi)
            pid=pi.autho.id
        return render(request,'myblog/editpost.html',{'form':form,'userid':userid,'pid':pid,'grp':grp,'fullname':fullname})

    else:
        return HttpResponseRedirect('/login/')


# Delet post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Blogpost.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')



