from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, null=True)
    email = models.EmailField(blank=True, null=True)


class Group(models.Model):
    name = models.CharField(max_length=20, blank=True)
    persons = models.ManyToManyField(Person, blank=True)
