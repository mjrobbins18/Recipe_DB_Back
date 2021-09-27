from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RecipeTitleCreateSerializer, MyTokenObtainPairSerializer, CustomUserSerializer, RecipeBodyCreateSerializer, RecipeViewSerializer, User, IngredientSerializer, EquipmentSerializer, ProcedureSerializer
from .models import Recipe, Ingredient, Procedure, Equipment, Post, Comment

# Delete, Update, Show, Recipe
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeViewSerializer

# List Recipe
class RecipeList(generics.ListCreateAPIView):
        queryset = Recipe.objects.all()
        serializer_class = RecipeViewSerializer
        permission_classes = (permissions.AllowAny,)
        authentication_classes = ()

# Create Recipe Title
class RecipeTitleCreate(generics.ListCreateAPIView):
        queryset = Recipe.objects.all()
        serializer_class = RecipeTitleCreateSerializer
        permission_classes = (permissions.AllowAny,)
        authentication_classes = ()
        
        def form_valid(self, form):
            form.instance.created_by = self.request.user
            return super(Recipe, self).form_valid(form)

#Create Recipe Body 
class RecipeBodyCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeBodyCreateSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()


class ObtainTokenPairWithNameView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    serializer_class = MyTokenObtainPairSerializer

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
# user views

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'

# Ingredient Views
class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

# Procedure Views
class ProcedureList(generics.ListCreateAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class ProcedureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    
# Equipment Views
class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
