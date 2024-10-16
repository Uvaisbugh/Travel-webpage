from django.db import models

# Create your models here.
class Place(models.Model):
    name =models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name

class Individual(models.Model):
    Pname = models.CharField(max_length=250)
    Pimg = models.ImageField(upload_to='per')
    Pdesc = models.TextField()

    def __str__(self):
        return self.Pname