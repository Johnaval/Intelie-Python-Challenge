from django.db import models
from datetime import datetime

# Create your models here.
'''class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published', default=datetime.now())
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name='Series', on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)
    
    def __str__(self):
        return self.tutorial_title

class Name(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Address(models.Model):
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address

class Entity(models.Model):
    entity_name = models.OneToOneField(Name, default=1, on_delete=models.CASCADE)
    entity_address = models.OneToOneField(Address, default=1, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Entities"

    def __str__(self):
        return f"Entity/{self.id}"

class Phone(models.Model):
    phone = models.CharField(max_length=200, unique=True)
    entity = models.ForeignKey(Entity, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.phone} : {self.entity}"

    def return_phone(self):
        return self.phone'''

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