from django.shortcuts import render
from app.forms import *
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
# Create your views here.

@login_required
def display_profile(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}                
    return render(request,'display_profile.html',d)

@login_required
def change_password(request):
    if request.method=="POST":
        username=request.session.get('username')
        password=request.POST['pw']
        UO=User.objects.get(username=username)
        UO.set_password(password)
        UO.save()
        return HttpResponse('the possword change sucssfully')
    return render(request,'change_password.html')
        
def forget_password(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pw']
        lUO=User.objects.filter(username=username)
        if lUO:
            lUO[0].set_password(password)
            lUO[0].save()
        else:
            return HttpResponse("user doesn't exist ")
        return HttpResponse('password change successfully')
    return render(request,'forget_password.html')



def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')



def mail(request):
    d={'UO':UserForm(),'PO':ProfileForm()}
    if request.method=='POST' and request.FILES:
        UFO=UserForm(request.POST)
        PFO=ProfileForm(request.POST,request.FILES)
        if UFO.is_valid() and PFO.is_valid():
            NSUO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            NSPO=PFO.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            send_mail('registration',
                      'succesfull',
                      'reddymalli988@gmail.com',
                      [NSUO.email],
                      fail_silently=True)
            return HttpResponse("data is inserted")
        else:
            return HttpResponse('invalid data')
    return render(request,'sendmail.html',d)

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("this is invalid data")
    return render(request,'user_login.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))