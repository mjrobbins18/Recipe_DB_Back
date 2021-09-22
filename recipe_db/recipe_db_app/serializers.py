from rest_framework import serializers
from .models import Ingredient, Recipe, Equipment, Procedure

# Ingredient serializer
class IngredientSerializer(serializers.ModelSerializer):
    recipe = serializers.HyperlinkedRelatedField(
        view_name='recipe_detail',
        read_only=True,
    )

    class Meta:
        model = Ingredient
        fields = ('id',
                  'name', 
                  'quantity', 
                  'unit_of_measure', 
                  'recipe',)

# Equipment Serializer
class EquipmentSerializer(serializers.ModelSerializer):
    recipe = serializers.HyperlinkedRelatedField(
        view_name='recipe_detail',
        read_only=True,
    )

    class Meta:
        model = Equipment
        fields = ('id',
                  'name', 
                  'quantity',
                  'recipe',)

# Procedure Serializer
class ProcedureSerializer(serializers.ModelSerializer):
    recipe = serializers.HyperlinkedRelatedField(
        view_name='recipe_detail',
        read_only=True,
    )

    class Meta:
        model = Procedure
        fields = ('id',
                  'step',
                  'recipe',)

# Recipe Serializer
class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(
        many=True,
        read_only=True
    )
    equipment = EquipmentSerializer(
        many=True,
        read_only=True
    )
    procedure = ProcedureSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Recipe
        fields = ('id',
                  'title',
                  'author', 
                  'image', 
                  'image_url',
                  'dish_components',
                  'author',
                  'category',
                  'ingredients',
                  'equipment',
                  'procedure',
                  )
