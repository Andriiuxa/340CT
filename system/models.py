from django.db import models

class stock(models.Model):
    album= models.CharField(max_length=250)
    album_title = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)


