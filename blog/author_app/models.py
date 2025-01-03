from django.db import models


class Author(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)
    birth_year = models.SmallIntegerField()
    biography = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"