from django.db import models

class information(models.Model):
    user_id=models.AutoField
    name=models.CharField(max_length=40,default="")
    roll_no=models.CharField(unique=True,default=0,max_length=15)
    branch=models.CharField(max_length=40,default=0)
    phone=models.CharField(default=0,max_length=12)
    password=models.CharField(max_length=30,default="")
    objects=models.Manager()