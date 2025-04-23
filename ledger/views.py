from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            return redirect('ledger:recipe-list')
    else:
        form = AuthenticationForm()
    return render(request, 'ledger/login.html', {'form': form})

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'

    login_url = '/login/'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
