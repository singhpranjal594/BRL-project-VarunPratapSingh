from django.db import models

class information(models.Model):
    user_id=models.AutoField
    name=models.CharField(max_length=40,default="")
    roll_no=models.IntegerField(default=0)
    branch=models.CharField(max_length=40,default=0)
    phone=models.IntegerField(default=0)
    password=models.CharField(max_length=30,default="")
    objects=models.Manager()