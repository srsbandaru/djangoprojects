from django.db import models

# Create your models here.

# Member model
class Member(models.Model):
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    mobileNumber = models.IntegerField(null=True)
    joinedDate = models.DateField(null=True)