from django.db import models
from django.contrib.auth.models import User




class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="مولف",blank=True,null=True,help_text=("Choose Auther"))
    date= models.DateTimeField()
    amount=models.BigIntegerField()
    text= models.CharField(max_length=255)

class Income(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="مولف",blank=True,null=True,help_text=("Choose Auther"))
    date= models.DateTimeField()
    amount=models.BigIntegerField()
    text= models.CharField(max_length=255)

class Token(models.Model):

     user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True,help_text=("Choose Auther"))   
     token= models.CharField(max_length=255) 