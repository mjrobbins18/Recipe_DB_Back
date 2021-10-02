from enum import unique
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Ingredient, Recipe, Equipment, Procedure, User, Favorites, RecipeBody, Comment, Post
from recipe_db_app import models

# Ingredient serializer
class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id',
                  'name', 
                  'quantity', 
                  'unit_of_measure', 
                  'recipe',)

# Equipment Serializer
class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ('id',
                  'name', 
                  'quantity',
                  'recipe',)

# Procedure Serializer
class ProcedureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procedure
        fields = ('id',
                  'step',
                  'recipe',)

class RecipeBodyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeBody
        fields = ('__all__')

# Favorite Serializer
class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorites
        fields=('id', 'recipe', 'user')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['first_name'] = user.first_name
        return token

# User Serializer

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(error_messages={})
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'id')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

     # Allows to search by username 
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
        
class RecipeTitleCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = '__all__'



# Recipe Serializer
class RecipeViewSerializer(serializers.ModelSerializer):
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
 
    recipe_body = RecipeBodyCreateSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = Recipe
        fields = ('id',
                  'title',
                  'recipe_body',
                  'user',
                  'ingredients',
                  'equipment',
                  'procedure',
                  )
     # Allows to search by username 
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(
        many=True,
        read_only=True
    )
   
    class Meta:
        model = Post
        fields = ('user',
                  'recipe',
                  'body',
                  'id',
                  'created_date',
                  'created_time',
                  'comments',
                  )

    # def get_object(self):
    #     queryset = self.get_queryset()             # Get the base queryset
    #     queryset = self.filter_queryset(queryset)  # Apply any filter backends
    #     filter = {}
    #     for field in self.lookup_fields:
    #         if self.kwargs[field]: # Ignore empty fields.
    #             filter[field] = self.kwargs[field]
    #     obj = get_object_or_404(queryset, **filter)  # Lookup the object
    #     self.check_object_permissions(self.request, obj)
    #     return obj