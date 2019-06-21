from django.db import models
from datetime import datetime

# Create your models here.
class Entry(models.Model):
    entity = models.IntegerField()
    attribute = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    date = models.DateTimeField('modified', default=datetime.now())
    validation = models.BooleanField()

    def __str__(self):
        return self.entity

class Schema(models.Model):
    attribute = models.CharField(max_length=200, unique=True)
    cardinality = models.CharField(max_length=4, choices=(('one', 'one'), ('many', 'many')), default='one')

    def __str__(self):
        return self.attribute