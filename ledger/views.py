from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Recipe

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ctx = {
        "recipe": recipe,
        "author": recipe.author.username,
        "ingredients": [
            {"name": ri.ingredient.name, "quantity": ri.quantity}
            for ri in recipe.ingredients.all()
        ],
    }
    return render(request, "ledger/recipe_detail.html", ctx)

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            return render(request, "users/login.html", {"error": "Username and password are required"})

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("recipe_list")
        else:
            return render(request, "users/login.html", {"error": "Invalid credentials"})

    return render(request, "users/login.html")


def custom_logout(request):
    logout(request)
    return redirect("custom_login")
