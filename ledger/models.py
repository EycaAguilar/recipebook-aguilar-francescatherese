from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ingredients = models.ManyToManyField('Ingredient')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])


class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="recipe_images/")
    description = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return f"Image for {self.recipe.name} - {self.description or 'No description'}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    short_bio = models.TextField(blank=True)

    def __str__(self):
        return self.full_name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="used_in_recipes")
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.name}"

    class Meta:
        unique_together = ('recipe', 'ingredient')
