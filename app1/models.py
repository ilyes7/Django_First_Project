from tabnanny import verbose
from django.db import models

# Create your models here.
class Client(models.Model):
    first_name= models.CharField(max_length=50)  #Varchar #<input type="text">
    dob= models.DateField()
    age= models.IntegerField(default=0)
   
class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    
    class Meta:
        verbose_name_plural = "Categories"
     
class Prodcut(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    desc = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
