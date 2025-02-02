from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_no=models.IntegerField("Employee Number", primary_key=True)
    birth_date=models.DateField("Birthday")
    first_name=models.CharField("First Name",max_length=14)
    last_name=models.CharField("Last Name", max_length=16)
    gender=models.CharField("Gender", max_length=1)
    hire_date=models.DateField("Hire Date")


    class Meta:
        db_table="employees"


    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
