from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Ingredient, Recipe, Equipment, Procedure, User, Favorites

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
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

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
    user = CustomUserSerializer(
        read_only=True
    )

    class Meta:
        model = Recipe
        fields = ('id',
                  'title', 
                  'image', 
                  'image_url',
                  'dish_components',
                  'user',
                  'category',
                  'ingredients',
                  'equipment',
                  'procedure',
                  )

# class UserSerializer(serializers.ModelSerializer):
#     created = serializers.DateTimeField(read_only=True)
#     updated = serializers.DateTimeField(read_only=True)
#     recipe = RecipeSerializer(
#         many=True,
#         read_only=True
#     )
#     favorites = FavoritesSerializer(
#         many=True,
#         read_only=True
#     )

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'is_active', 'created', 'updated', 'recipe', 'favorites']
#         read_only_field = ['is_active']
