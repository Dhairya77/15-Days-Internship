from django.db import models
from django.db.models.aggregates import Aggregate

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mo_no = models.IntegerField(max_length=10)
    email = models.CharField(max_length=30)
    hd_orphan = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name

class Student(Person):
    School = models.CharField(max_length=50)
    College = models.CharField(max_length=50)
    Aggregate = models.FloatField(max_length=5)

    def __str__(self):
        return self.first_name