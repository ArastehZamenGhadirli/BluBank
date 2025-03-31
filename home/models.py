from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=20)

class Account(models.Model):
    name = models.CharField(max_length=100)
    user =  models.OneToOneField(User , on_delete=models.CASCADE)
    national_id = models.CharField(max_length=11, unique=True)
    
class Profit(models.Model):
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=20 , unique=True)
    duration = models.IntegerField()
    account = models.ForeignKey(to=Account,on_delete=models.CASCADE,related_name="Account_Profit")









    
    


        
    


