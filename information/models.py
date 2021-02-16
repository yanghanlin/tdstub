from django.db import models
from .core.entity import Entity


class Instance(models.Model, Entity):
    uid = models.CharField('Unique identifier', max_length=255, editable=False, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.uid

    def data(self):
        return {
            'uid': self.uid,
            'description': self.description,
        }


class EventTag(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)


class Event(models.Model):
    timestamp = models.DateTimeField(auto_created=True, null=False)
    description = models.TextField()
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    tags = models.ManyToManyField(EventTag)
