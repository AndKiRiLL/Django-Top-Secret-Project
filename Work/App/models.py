from django.db import models

class Films(models.Model):
    name = models.CharField(max_length=35)
    category = models.CharField(max_length=35)
    date_create = models.CharField(max_length=35)
    actors = models.TextField()
    date_visible = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Category(models.Model):
    name_category = models.CharField(max_length=35)

    def __str__(self):
        return self.name_category

