from django.db import models
from datetime import datetime
# Create your models here.

departments = [('Select Department', 'Select Department'),
('Cardiologist', 'Cardiologist'),
('Dermatologists', 'Dermatologists'),
('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
('Allergists/Immunologists', 'Allergists/Immunologists'),
('Anesthesiologists', 'Anesthesiologists'),
('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
]
gen = [('Select Gender', 'Select Gender'),('Male', 'Male'),('Female', 'Female')]
exp= [('Select Experience', 'Select Experience'), ('2 years', '2 years'),('3 years', '3 years'),
      ('4 years', '4 years'),('5 years', '5 years'),('More than', 'More than')]


class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50,choices=departments,default=' ')

    def __str__(self):
        return self.Name
      

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=gen, default=' ')
    mobile = models.IntegerField(null=True)
    address = models.TextField()

    def __str__(self):
        return self.name


class Nurse(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    experience = models.CharField(max_length=50,choices=exp,default=' ')

    def __str__(self):
        return self.Name    


class Operation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    department = models.CharField(max_length=50,choices=departments,default='') 
    date = models.DateField(blank=True, null=True)
    # birthdate = models.DateTimeField(blank=True, null=True)   
    time = models.TimeField()

    def __str__(self):
        return self.department
    


class Nurse_List(models.Model):

    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)

    def __str__(self):
        return self.nurse