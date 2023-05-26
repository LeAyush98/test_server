from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER = [("Male", "Male"), ("Female" ,"Female")]
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=30, choices=GENDER)

    def __str__(self) -> str:
        return self.name