from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blogpost(models.Model):
    title=models.CharField(max_length=133)
    desc=models.TextField()
    autho = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
