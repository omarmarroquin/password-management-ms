from django.db import models

# Create your models here.
class Password(models.Model):
  url = models.URLField(max_length = 200)
  name = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  password = models.TextField()
