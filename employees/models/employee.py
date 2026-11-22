from django.db import models

class Gender(models.TextChoices):
    MALE='MALE','male'
    FEMALE='FEMALE','female'
    OTHER='OTHER','other'

class Employee(models.Model):
    emp_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=10,choices=Gender.choices)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=13)
    date_of_birth=models.DateField()

    class Meta:
        db_table='employees'