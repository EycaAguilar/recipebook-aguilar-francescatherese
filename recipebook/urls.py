from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include('ledger.urls')),
    path('', lambda request: redirect('ledger:recipe-list')),
]