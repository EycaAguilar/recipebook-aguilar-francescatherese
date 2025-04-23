from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RecipeListView, RecipeDetailView

app_name = 'ledger'

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='ledger/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='ledger:recipe-list'), name='logout'),
]

