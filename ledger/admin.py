from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline, RecipeIngredientInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeImage)
admin.site.register(Ingredient)
