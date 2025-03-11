from ledger.models import Recipe, Ingredient, RecipeIngredient

tomato = Ingredient.objects.create(name="Tomato")
onion = Ingredient.objects.create(name="Onion")
pork = Ingredient.objects.create(name="Pork")

sinigang = Recipe.objects.create(name="Sinigang")

# Link ingredients to the recipe
RecipeIngredient.objects.create(recipe=sinigang, ingredient=tomato, quantity="3 pcs")
RecipeIngredient.objects.create(recipe=sinigang, ingredient=onion, quantity="1 pc")
RecipeIngredient.objects.create(recipe=sinigang, ingredient=pork, quantity="1 kg")

print("Database populated successfully!")
