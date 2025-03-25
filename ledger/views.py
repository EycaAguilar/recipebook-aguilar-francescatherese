from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from .forms import RecipeForm

@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()

    return render(request, "ledger/add_recipe.html", {"form": form})

class RecipeImageUploadView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ["image", "description"]
    template_name = "ledger/recipe_image_form.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={'recipe_id': self.object.recipe.id})


@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = [
        {"name": ri.ingredient.name, "quantity": ri.quantity}
        for ri in recipe.recipe_ingredients.all()
    ]

    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            return render(request, "ledger/login.html", {"error": "Username and password are required"})

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("recipe_list")
        else:
            return render(request, "ledger/login.html", {"error": "Invalid credentials"})

    return render(request, "ledger/login.html")

def custom_logout(request):
    logout(request)
    return redirect("login")
