from django.db import models

# Create your models here.
class formdata(models.Model):
    fname = models.CharField(max_length=100)
    eads=models.CharField(max_length=100)
    mnb=models.CharField(max_length=100)
    esub=models.CharField(max_length=100)
    ym=models.CharField(max_length=100)

    def __str__(self):
        return self.fname

class pictures(models.Model):
    img=models.ImageField(upload_to="mipics/")