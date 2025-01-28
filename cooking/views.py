from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class RecipesListView(generic.ListView):
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes_list'
    model = models.RecipeModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class RecipeDetailView(generic.DetailView):
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'
    model = models.RecipeModel

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)


class CreateNewRecipeView(generic.CreateView):
    template_name = 'recipes/create_recipe.html'
    form_class = forms.RecipeForm
    success_url = '/recipes_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateNewRecipeView, self).form_valid(form=form)


class UpdateRecipeView(generic.UpdateView):
    template_name = 'recipes/create_recipe.html'
    form_class = forms.RecipeForm
    success_url = '/recipes_list/'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)


class RecipeDeleteView(generic.DeleteView):
    template_name = 'recipes/confirm_delete.html'
    success_url = '/recipes_list/'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)


class IngredientCreateView(generic.CreateView):
    template_name = 'recipes/ingredient_form.html'
    form_class = forms.IngredientForm

    def form_valid(self, form):
        recipe_id = self.kwargs.get('recipe_id')
        recipe = get_object_or_404(models.RecipeModel, id=recipe_id)
        ingredient = form.save(commit=False)
        ingredient.recipe = recipe
        ingredient.save()
        return super().form_valid(form)

    def get_success_url(self):
        return f"/recipes_list/{self.kwargs.get('recipe_id')}/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_id = self.kwargs.get('recipe_id')
        recipe = get_object_or_404(models.RecipeModel, id=recipe_id)
        context['recipe'] = recipe
        return context