from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('', recipe_list, name='recipe-list'),
    path('<int:pk>/', recipe_detail, name='recipe-detail'),
]


app_name = 'ledger'
