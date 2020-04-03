from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=40,null=True, blank=True)
    userId=models.IntegerField(blank=True,null=True)
    role=models.IntegerField()
    isActive=models.BooleanField(default=False)
    createdDate=models.DateTimeField(auto_now=False,auto_now_add=True)
    updatedDate=models.DateTimeField(auto_now=True,auto_now_add=False)

class Questions(models.Model):
    qustion=models.CharField(max_length=100)
    option1=models.CharField( max_length=50)
    option2=models.CharField( max_length=50)
    option3=models.CharField( max_length=50)
    option4=models.CharField( max_length=50)
    isActive=models.BooleanField(default=False)
    createdDate=models.DateTimeField(auto_now=False,auto_now_add=True)
    updatedDate=models.DateTimeField(auto_now=True,auto_now_add=False)

class UserAnswer(models.Model):
    Questions=models.ForeignKey(Questions,on_delete=models.Empty,null=True, blank=True)
    QuID=models.IntegerField(null=True, blank=True)
    userAns=models.IntegerField()
    Register=models.ForeignKey(Register, on_delete=models.CASCADE,null=True, blank=True)
    userid=models.IntegerField(null=True,blank=True)
    isActive=models.BooleanField(default=False)
    createdDate=models.DateTimeField(auto_now=False,auto_now_add=True)
    updatedDate=models.DateTimeField(auto_now=True,auto_now_add=False)

class FriendsAnswer(models.Model):
    name=models.CharField(max_length=50)
    score=models.IntegerField()
    Register=models.ForeignKey(Register, on_delete=models.CASCADE)