from django.db import models

class Search(models.Model):
    destination = models.CharField(max_length=120) #max length is required
