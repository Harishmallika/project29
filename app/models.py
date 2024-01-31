from django.db import models

# Create your models here.

class School(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    slocation=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    email=models.EmailField(default='hai@gmail.com')
    renteremail=models.EmailField(default='hai@gmail.com')

    def __str__(self):
        return self.sname
