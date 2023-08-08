from django.db import models

# Create your models here.
class Student(models.Model):
    s_name=models.CharField(max_length=100)
    s_age=models.IntegerField()
    s_dept=models.CharField(max_length=30)


