from uuid import UUID
import uuid
from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    director_id = models.UUIDField(default=uuid.uuid1, editable=False, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    actor_id = models.UUIDField(default=uuid.uuid1, editable=False, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Movie(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    grade = models.FloatField(verbose_name='grade', default=0)
    year = models.DateField()
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    img_id = models.UUIDField(default=uuid.uuid1, editable=False, unique=True)

    def __str__(self):
        return self.name

    def get_director(self):
        return self.director