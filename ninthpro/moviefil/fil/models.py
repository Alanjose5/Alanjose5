from django.db import models


# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    year = models.DateField()
    image = models.ImageField(upload_to="img")