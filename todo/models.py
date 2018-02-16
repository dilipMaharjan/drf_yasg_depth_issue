from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)


class TodoAnother(models.Model):
    todo = models.ForeignKey(Todo, on_delete=True)
    title = models.CharField(max_length=50)


class TodoYetAnother(models.Model):
    todo = models.ForeignKey(TodoAnother, on_delete=True)
    title = models.CharField(max_length=50)
