from django.db import models
from django.conf import settings




class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name="مولف",blank=True,null=True,help_text=("Choose Auther"))
    date= models.DateTimeField()
    amount=models.BigIntegerField()
    text= models.CharField(max_length=255)
