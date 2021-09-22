
from django.db import models


class Callback(models.Model): 
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30, blank= True)
    company = models.CharField(max_length=100, blank= True)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    problem_desc = models.TextField(max_length=1000)
    date_and_time = models.DateTimeField(blank= True)


