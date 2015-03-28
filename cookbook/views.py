from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from cookbook.models import Recipe, Ingredient


def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}
    return render(request, 'cookbook/index.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    total = 0
    for ingredient in recipe.ingredients.all():
        total += ingredient.calorie_count
    return render(request, 'cookbook/detail.html', {'recipe': recipe,
                  'total_calories': total})

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
