from django.db import models

# Create your models here.
class formdata(models.Model):
    uname=models.CharField(max_length=10)
    em=models.CharField(max_length=20)
    sub=models.CharField(max_length=100)
    mes=models.CharField(max_length=100)

    def __str__(self):
        return self.uname
    

class pictures(models.Model):
    img =models.ImageField(upload_to="mypics/")
    img1 =models.ImageField(upload_to="mypics1/")


