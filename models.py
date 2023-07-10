from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Visitor(models.Model):
    visitorname = models.CharField(max_length=100,null=True)
    mobileno = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    apartment = models.CharField(max_length=100,null=True)
    floor = models.CharField(max_length=50,null=True)
    whomtomeet = models.CharField(max_length=100,null=True)
    reasontomeet = models.CharField(max_length=200,null=True)
    intime = models.CharField(max_length=50,null=True)
    vdate = models.DateField(null=True)
    remark = models.CharField(max_length=500,null=True)
    outtime = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.visitorname



