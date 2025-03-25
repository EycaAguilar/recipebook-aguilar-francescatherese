from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("", views.recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_id>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/add/", views.add_recipe, name="add_recipe"),
    path("recipe/<int:pk>/upload_image/", views.RecipeImageUploadView.as_view(), name="recipe-add-image"),  # Image upload URL
]

