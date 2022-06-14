from django.db import models

class SizeCategory(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=60)

    def __str__(self):
        return self.description

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    categories = models.ManyToManyField(SizeCategory)
    
    def __str__(self):
        return self.name

