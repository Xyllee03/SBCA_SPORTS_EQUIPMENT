from django.db import models

# Create your models here.



class StudentBorrow(models.Model):
    id =models.AutoField(primary_key=True)
    student_no = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    code_request = models.CharField(max_length=20, blank=True, null=True)

class ItemRequest(models.Model):
    id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(max_length=255)
    quantity = models.IntegerField(blank=True, null=True)
    id_student_borrow = models.ForeignKey(StudentBorrow, on_delete=models.CASCADE)
    