from django.db import models

# Create your models here.
class car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    offer = models.BooleanField(default=False)
    abc = models.IntegerField()