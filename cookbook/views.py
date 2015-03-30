from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from cookbook.models import Recipe

class RecipeList(ListView):
    model = Recipe

class RecipeCreate(CreateView):
    model = Recipe
    success_url = reverse_lazy('cookbook:recipe_list')

class RecipeUpdate(UpdateView):
    model = Recipe
    success_url = reverse_lazy('cookbook:recipe_list')

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('cookbook:recipe_list')

class RecipeDetail(DetailView):
    model = Recipe
    # TODO -- How do I access the pk for the current recipe? Remove hard-coded value
    recipe = get_object_or_404(Recipe, pk=1)
    template_name = 'cookbook/detail.html'
    total = model.get_total_calories(recipe)
    context = {'recipe_id': recipe.id}
