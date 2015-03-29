from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView

from cookbook.models import Recipe, Ingredient


class RecipeMixin(object):
    def get_total_calories(self):
        recipe = get_object_or_404(Recipe, pk=1)
        total = 0
        for ingredient in recipe.ingredients.all():
            total += ingredient.calorie_count
        return total

class RecipeList(RecipeMixin, ListView):
    template_name = 'cookbook/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.all
    # recipe_list = Recipe.objects.all()
    # context = {'recipe_list': recipe_list}
    # return render(request, 'cookbook/index.html', context)


class RecipeDetail(RecipeMixin, DetailView):
    model = Recipe
    template_name = 'cookbook/detail.html'
    # def get_queryset(self):
    #     self.recipe = get_object_or_404(Recipe, pk=1)
    #     return Ingredient.objects.filter(recipe=self.recipe.id)

    # return render(request, 'cookbook/detail.html', {'recipe': recipe,
    #               'total_calories': total})

def edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        new_title = request.POST['title']
        recipe.title = new_title
        recipe.save()
        return HttpResponseRedirect(reverse('cookbook:detail', args=(recipe.id,)))
    # for incorporating post response form
    #     form = RecipeEditForm(request.POST)
    #     if form.is_valid():
    #         # process the data in form as required
    #         # ...
    #         # redirect
    #         return HttpResponseRedirect('cookbook/detail.html', {'recipe': recipe})
    # print "******** %r", request.POST['recipe__title']
    return render(request, 'cookbook/edit.html', {'recipe': recipe})

def delete(request, recipe_id):
    pass

def new(request):
    pass

# potential method to calculate a recipe's total_calories
# def total_calories(self):
#     total = 0
#     for ingredient in recipe.ingredients.all():
#         total += ingredient.calorie_count
#     return total
