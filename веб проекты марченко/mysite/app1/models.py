from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    age = models.IntegerField()
    date_of_birth = models.DateField(null=False)
    patronymic = models.CharField(max_length=120, null=True)
    Salary = models.FloatField(null=False)
