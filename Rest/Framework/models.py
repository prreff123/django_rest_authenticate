from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=20)    

class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=20,default='')
    roll_no = models.CharField(max_length=20,default=0)