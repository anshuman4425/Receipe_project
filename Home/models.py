from django.db import models

# Create your models here.
class student(models.Model):
    name= models.CharField(max_length=50)
    age= models.IntegerField()
    roll_no= models.IntegerField(default=0)
    email= models.EmailField()
