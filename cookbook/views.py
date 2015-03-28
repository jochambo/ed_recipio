from django.http import Http404
from django.shortcuts import get_object_or_404, render

from cookbook.models import Recipe, Ingredient


def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}
    return render(request, 'cookbook/index.html', context)
