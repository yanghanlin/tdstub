from django.db import models


class Instance(models.Model):
    uid = models.CharField('Unique identifier', max_length=255, editable=False, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.uid


class EventTag(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)


class Event(models.Model):
    timestamp = models.DateTimeField(auto_created=True, null=False)
    description = models.TextField()
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    tags = models.ManyToManyField(EventTag)
