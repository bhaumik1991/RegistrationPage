        from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from signup.models import Student

from django.conf import settings
from .forms import userform

def signup(request):
    if request.method == 'POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['user_name']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            emailid = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username = user_name, first_name = first_name, last_name =last_name,email = emailid, password = password)
            messages.success(request,'Registration Successfull')
            usr = auth.authenticate(username = user_name, password = password)
            auth.login(request,usr)
            #return HttpResponseRedirect('/signup/signup/')
            return render(request, 'welcome.html')
    else:
        form1 = userform()
    return render(request,'signup.html',{'frm':form1})
def login(request):
    if request.method == 'POST':
        form1 = loginform(request.POST)
        #username = form2.cleaned_data['username']
        xyz = request.POST['username']
        #emailid = request.POST['email']
        #password = form2.cleaned_data['password']
        password = request.POST['password']
        try:
            user = auth.authenticate(username = xyz, password = password)
            if user is not None:
                auth.login(request, user)
                return render(request,'welcome.html')
            else:
                messages.error(request,'Ivalid username or password!')
        except ObjectDoesNotExist:
            print("Invalid user")
    else:
        form1 = loginform()
    return render(request, 'login.html',{'frm':form1})

def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
