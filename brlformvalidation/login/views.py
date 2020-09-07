from django.shortcuts import render
from signup.models import information

def index(request):
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
