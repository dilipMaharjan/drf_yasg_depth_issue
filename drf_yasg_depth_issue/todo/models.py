from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class A(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return '{}'


class C(models.Model):
    title = models.CharField(max_length=50)
    p = models.ForeignKey(
        "P",
        on_delete=models.CASCADE
    )
    co = GenericRelation("Co")

    def __str__(self):
        return '{}'


class Chu(models.Model):
    title = models.CharField(max_length=50)
    c = models.ForeignKey(C, on_delete=models.CASCADE)
    comments = GenericRelation("Co")

    def __str__(self):
        return '{}'


class Co(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return '{}'


class P(models.Model):
    title = models.CharField(max_length=50)
    a = models.ForeignKey("A", on_delete=models.CASCADE)


class T(models.Model):
    title = models.CharField(max_length=50)
    chu = models.ForeignKey("Chu", on_delete=models.CASCADE)
    co = GenericRelation("Co")
