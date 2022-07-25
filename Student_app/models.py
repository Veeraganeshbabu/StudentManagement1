from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Details(models.Model):
    StudentId = models.CharField(max_length=200, null=True)
    StudentName = models.CharField(max_length=50, null=True)
    Phone = models.IntegerField(null=True)
    Email = models.CharField(max_length=50,null=True)
    DateOfBirth = models.DateField()
    Graduation = models.CharField(max_length=100,null=True)
    YearOfPass = models.IntegerField( null=True)
    BatchName = models.CharField(max_length=100)


    def __str__(self):
        return self.StudentName
