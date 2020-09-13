from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .models import information
from rest_framework import viewsets
from .serializers import informationserializer

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
            return(render(request,'error1.html'))

    else:
        return(render(request,'signup.html'))
class informationviewset(viewsets.ModelViewSet):
    queryset=information.objects.all()
    serializer_class=informationserializer
def login(request):
    if request.method == "POST":
        rollno=request.POST['rollno']
        password=request.POST['password']
        user=information.objects.get(roll_no=rollno)
        print(user)
        if user:
            if password == user.password:
                return(render(request,'done.html'))
            else:
                return(render(request,'error.html'))
        else:
            return(render(request,'error.html'))
    else:
        return(render(request,'login.html'))


