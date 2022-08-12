from django.db import models

# Create your models here.

class DataModel(models.Model):
    name = models.CharField(name="name", max_length=256)
    text = models.TextField(name="text", default="")
