from django.db import models

# Create your models here.
class Users(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=100,default='M',help_text='M=male,F=female,O=others')
    phone_no=models.IntegerField(default=None)
    created_by=models.IntegerField(max_length=11,default=None)
    modified_by=models.IntegerField(max_length=11,default=None)

    def _str_(self):
        return self.firstname
