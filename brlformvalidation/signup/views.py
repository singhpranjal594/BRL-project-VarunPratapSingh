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
        rollnol=information.objects.all().values('roll_no')
        a=False
        for i in rollnol:
            if i == roll_no:
                a=True
                break
        if a:
            return HttpResponse("eror rollno already exsists")
        else:
            info=information(name=name,password=password,roll_no=roll_no,phone=phone,branch=branch)
            info.save()
            return(render(request,'index.html'))

    else:
        return(render(request,'index.html'))