from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def HomePage(request):
    #return render(request,'/home/vibha/Downloads/source_code_final/entries/urls.py')
    return render(request,'entry_list.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            # messages.success(request,"Your account has been successfully created")
            return redirect('login')
        #print(uname,email,pass1,pass2)

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')

        user=authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/main/')
        else:
            # messages.error(request, "Bad credentials")
            return redirect('login')
        # if(username==uname & pass3==pass1):
        # return HttpResponseRedirect('/main/')
        # return redirect(reverse('entry_list'))
    return render (request,'login.html')

def logout(request):
    logout(request)
    
    
    return redirect('login')
