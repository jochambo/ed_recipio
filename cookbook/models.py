from django.db import models


class Ingredient(models.Model):
    """
    Has the text of the ingredient and a calorie_count.
    """
    title = models.CharField(max_length=200)
    calorie_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Recipe(models.Model):
    """
    Has a title.
    Is associated with a recipe.
    """
    title = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)

    def __unicode__(self):
        return self.title
