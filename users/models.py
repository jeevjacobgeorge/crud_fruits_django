from django.db import models

# Create your models here.
from django.db import models

class Nutrition(models.Model):
    calories = models.FloatField()
    fat = models.FloatField()
    sugar = models.FloatField()
    carbohydrates = models.FloatField()
    protein = models.FloatField()

    def __str__(self):
        return f"Nutrition (Calories: {self.calories}, Protein: {self.protein})"

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    order = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    nutrition = models.OneToOneField(Nutrition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
