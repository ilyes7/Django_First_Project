from django.db import models
from django.core.validators import *


EMAIL_REGEX = RegexValidator(r'[A-Za-z0-9._%+-]+@esprit.tn$', 'only valid email is required')
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(
        validators=[EMAIL_REGEX]
    )
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Student(User):
    pass

class Coach(User):
    pass

class Project(models.Model):
    name = models.CharField(verbose_name="Project name",max_length=50)
    duration = models.IntegerField()
    time_allocated = models.IntegerField(
        validators=[
            MinValueValidator(1,"The minimum value must be 1"),
            MaxValueValidator(100,"The maximum value must be 100")
        ]
    )
    besoin = models.TextField(max_length=250)
    desc = models.TextField(max_length=250)
    isValid = models.BooleanField(default=False)
    creator = models.OneToOneField(
        Student,
        on_delete = models.CASCADE,
        related_name="creator"
    )
    supervisor = models.ForeignKey(
        Coach,
        on_delete=models.CASCADE,
        related_name="supervisor"
        
    )
    members = models.ManyToManyField(
        Student,
        through="memberShip", #Table associative        
        related_name="members"
        
    )
    
class memberShip(models.Model):
    Project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,

    )
    Student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    allocated_time_by_member = models.IntegerField(default=0)
