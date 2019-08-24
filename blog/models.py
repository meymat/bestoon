from django.db import models
from django.contrib.auth.models import User




class Expense(models.Model):
    user =        models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="مولف",blank=True,null=True,help_text=("Choose Auther"))
    date=         models.DateTimeField()
    amount=       models.BigIntegerField()
    text=         models.CharField(max_length=255)

class Income(models.Model):
    user =        models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="مولف",blank=True,null=True,help_text=("Choose Auther"))
    date=         models.DateTimeField()
    amount=       models.BigIntegerField()
    text=         models.CharField(max_length=255)

class Token(models.Model):

    user =        models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True,help_text=("Choose Auther"))   
    token=        models.CharField(max_length=255) 


class Passwordresetcodes(models.Model):
    code =        models.CharField(max_length=32)
    email =       models.CharField(max_length = 120)
    time =        models.DateTimeField()
    username =    models.CharField(max_length=50)
    password =    models.CharField(max_length=50) #TODO: do not save password    