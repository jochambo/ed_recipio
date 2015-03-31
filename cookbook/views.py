from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

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
    template_name = 'cookbook/detail.html'
    # context = {}

    # def get(self, request, *args, **kwargs):
    #     print kwargs.get('pk', None)
    #     # TODO -- How do I access the pk for the current recipe? Remove hard-coded value
    #     recipe = get_object_or_404(Recipe, pk=kwargs.get('pk', None))
    #     total = recipe.get_total_calories()
    #     self.context["total"] = total
    #     return super(RecipeDetail, self).get(request, *args, **kwargs)
