from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .models import information
    

def index(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        roll_no=request.POST['rollno']
        phone=request.POST['phone']
        branch=request.POST['branch']
        info=information(name=name,password=password,roll_no=roll_no,phone=phone,branch=branch)
        try:
            info.save()
            return(render(request,'signup.html'))
        except:
            return(render(request,'error.html'))

    else:
        return(render(request,'signup.html'))