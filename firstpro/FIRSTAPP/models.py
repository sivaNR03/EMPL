from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confrmpassword = models.CharField(max_length=100)
   

  



        