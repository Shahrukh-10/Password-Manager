from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False,unique=True)
    mainpass = models.CharField(max_length=100,null=False,blank=False)
    
    def __str__(self):
        return self.username

class Password(models.Model):
    userinfo = models.ForeignKey(Account,on_delete=models.CASCADE)
    email = models.CharField(max_length=100,null=False,blank=False)
    password = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.email