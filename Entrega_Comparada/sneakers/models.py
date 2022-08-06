from django.db import models

class Jordans(models.Model):
    model=models.CharField(max_length=40)
    price=models.IntegerField()
    coulor=models.CharField(max_length=40)
    description=models.CharField(max_length=400,null=True)
    year=models.IntegerField(null=True)
    stock=models.IntegerField(null=True)

class Air_Force(models.Model):
    model=models.CharField(max_length=40)
    price=models.IntegerField()
    coulor=models.CharField(max_length=40)
    description=models.CharField(max_length=400,null=True)
    year=models.IntegerField(null=True)
    stock=models.IntegerField(null=True)

def __str__(self):
        return self.name

