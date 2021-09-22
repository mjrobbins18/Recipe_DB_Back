from django.shortcuts import render
from rest_framework import generics
from .serializers import RecipeSerializer,IngredientSerializer,EquipmentSerializer,ProcedureSerializer
from .models import Recipe, Ingredient, Equipment, Procedure

# Recipe Views
class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

# # Ingredient Views
# class IngredientList(generics.ListCreateAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer

# class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer

# # Procedure Views
# class RecipeList(generics.ListCreateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer

# class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
    
# # Equipment Views
# class RecipeList(generics.ListCreateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer

# class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
