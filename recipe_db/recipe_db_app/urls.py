from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='recipe_list'),
    path('recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
]