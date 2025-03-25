from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from ledger.views import recipe_list, recipe_detail, RecipeImageUploadView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="ledger/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", recipe_list, name="recipe_list"),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/add_image/', RecipeImageUploadView.as_view(), name='recipe-add-image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
