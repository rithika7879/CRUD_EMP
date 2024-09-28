from django.db import models

class Employee(models.Model):
    # Fields for Employee
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    phone_number = models.IntegerField()
    location = models.CharField(max_length=100)
    
def __str__(self):
    return self.name

