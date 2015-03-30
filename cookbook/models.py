from django.db import models
from django.core.urlresolvers import reverse


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

    def get_absolute_url(self):
        return reverse('recipe_edit', kwargs={'pk': self.pk})

    def get_total_calories(self):
        total = 0
        for ingredient in self.ingredients.all():
            total += ingredient.calorie_count
            print "**** Total: %d" % total
        return total

# TODO -- Implement ordering based on total calories
    # class Meta:
    #     ordering = get_total_calories()
