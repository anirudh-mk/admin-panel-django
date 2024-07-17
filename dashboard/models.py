import uuid

from django.db import models

# Create your models here.


class Actor(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Movies(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4())
    title = models.CharField(max_length=200)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)