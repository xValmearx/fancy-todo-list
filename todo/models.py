from django.db import models


class Todo(models.Model):
    """Todo model class"""

    name = models.CharField(max_length=150)
    complete_by_datetime = models.CharField(max_length=50)

    def __str__(self):
        return self.name[50]
