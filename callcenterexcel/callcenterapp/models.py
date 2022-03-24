from locale import T_FMT
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField


#----------------------------------------------------
class Designation(models.Model):
    designation=models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.designation


#---------------------------------------------User model----------------------------------------------
class User(AbstractUser):
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True)
    password = models.CharField(max_length=255)
    username=models.CharField(max_length=255,unique=True,null=True)
    first_name=None
    last_name=None
    designation=models.ForeignKey(Designation,on_delete=models.CASCADE,null=True,blank=True)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []



class Status(models.Model):
    status_value=models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.status_value


class Customerdetails(models.Model):
     name=models.CharField(max_length=200,null=True)
     phone=models.CharField(max_length=15,null=True)
     religion=models.CharField(max_length=200,null=True)
     cast=models.CharField(max_length=200,null=True)
     district=models.CharField(max_length=200,null=True)
     feedback=models.CharField(max_length=500,null=True)
     gender=models.CharField(max_length=500,null=True)
     age=models.IntegerField(null=True)
     status=models.ForeignKey(Status,default=10,on_delete=models.CASCADE,null=True)
     remarks=models.CharField(max_length=500,null=True)
     followup=models.DateField(null=True)
     telecall=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     flag=models.IntegerField(default=0,null=True)

     class Meta:
        ordering = ['id']
     def __str__(self):
         return self.name
     

class ExcelFileupload(models.Model):
    excel_file_upload=models.FileField(upload_to="excel")





class Followupcustomerdetails(models.Model):
     name=models.CharField(max_length=200,null=True)
     phone=models.CharField(max_length=15,null=True)
     religion=models.CharField(max_length=200,null=True)
     cast=models.CharField(max_length=200,null=True)
     district=models.CharField(max_length=200,null=True)
     feedback=models.CharField(max_length=500,null=True)
     gender=models.CharField(max_length=500,null=True)
     age=models.IntegerField(null=True)
     status=models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
     remarks=models.CharField(max_length=500,null=True)
     followup=models.DateField(null=True)
     telecall=models.CharField(max_length=500,null=True)
     flag=models.IntegerField(default=0,null=True)
     is_followup=models.BooleanField(default=True,null=True)

     class Meta:
        ordering = ['id']
     def __str__(self):
         return self.name