from sys import maxsize
from urllib.parse import MAX_CACHE_SIZE
from django.db import models

# Create your models here.
class stud(models.Model):
    s_name = models.CharField(max_length = 30)
    s_class = models.CharField(max_length = 30)
    s_address = models.CharField(max_length = 30)
    s_school = models.CharField(max_length = 30)
    s_email = models.CharField(max_length = 30)
    

    