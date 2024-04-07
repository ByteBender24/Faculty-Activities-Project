import os
from django.db import models

class AdminLogin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class FacultyLogin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class SDP_attended(models.Model):
    staff_attended=models.CharField(max_length=100)
    nature_of_event=models.CharField(max_length=100)
    type_of_event=models.CharField(max_length=100)
    name_of_event=models.CharField(max_length=100)
    conducted_by=models.CharField(max_length=100)
    no_of_days=models.IntegerField()
    duration=models.CharField(max_length=100)
    proof_document=models.FileField(upload_to='proof/', max_length=250)
    academic_year=models.CharField(max_length=100)
    
class SDP_organised(models.Model):
    staff_attended=models.CharField(max_length=1000)
    type_of_event=models.CharField(max_length=100)
    name_of_event=models.CharField(max_length=200)
    duration=models.CharField(max_length=100)
    no_of_participants=models.IntegerField()
    resource_persons=models.CharField(max_length=1000)
    name_of_sponsors=models.CharField(max_length=200)