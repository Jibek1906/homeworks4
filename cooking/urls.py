from django.urls import path
from . import views

urlpatterns = [
    path('create_recipe/', views.CreateNewRecipeView.as_view(), name='add_recipe'),
    path('recipes_list/', views.RecipesListView.as_view(), name='recipes_list'),
    path('recipes_list/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes_list/<int:id>/update/', views.UpdateRecipeView.as_view(), name='update_recipe'),
    path('recipes_list/<int:id>/delete/', views.RecipeDeleteView.as_view(), name='delete_recipe'),
    path('recipes_list/<int:recipe_id>/add_ingredient/', views.IngredientCreateView.as_view(), name='add_ingredient'),
]