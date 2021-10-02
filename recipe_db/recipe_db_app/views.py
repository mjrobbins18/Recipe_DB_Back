from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .serializers import RecipeTitleCreateSerializer, MyTokenObtainPairSerializer, CustomUserSerializer, RecipeBodyCreateSerializer, RecipeViewSerializer, User, IngredientSerializer, EquipmentSerializer, ProcedureSerializer, CommentSerializer, PostSerializer
from .models import Recipe, Ingredient, Procedure, Equipment, Post, Comment, RecipeBody

# Delete, Update, Show, Recipe
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeViewSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()    

# List Recipe
class RecipeList(generics.ListCreateAPIView):
        queryset = Recipe.objects.all()[:12]
        serializer_class = RecipeViewSerializer
        permission_classes = (permissions.AllowAny,)
        authentication_classes = ()    


# get recipes by username
class RecipeListByUser(generics.ListCreateAPIView):
        queryset = Recipe.objects.all()
        serializer_class = RecipeViewSerializer
        permission_classes = (permissions.AllowAny,)
        authentication_classes = ()

        def get_queryset(self):
            user = self.kwargs['user']
            return Recipe.objects.filter(user=user)

# get recipes by title
class RecipeListByTitle(generics.ListCreateAPIView):
        queryset = Recipe.objects.all()
        serializer_class = RecipeViewSerializer
        permission_classes = (permissions.AllowAny,)
        authentication_classes = ()

        def get_queryset(self):
            title = self.kwargs['title']
            return Recipe.objects.filter(title=title)

# recipe search
class RecipeSearch(generics.ListCreateAPIView):
    serializer_class = RecipeViewSerializer
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  Recipe.objects.filter(Q(title__icontains=query))[:10]
        return object_list


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
    queryset = RecipeBody.objects.all()
    serializer_class = RecipeBodyCreateSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def form_valid(self, form):
            form.instance.created_by = self.request.user
            return super(RecipeBody, self).form_valid(form)


# Delete, Update, Show, Recipe Body
class RecipeBodyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeBody.objects.all()
    serializer_class = RecipeBodyCreateSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def form_valid(self, form):
            form.instance.created_by = self.request.user
            return super(RecipeBody, self).form_valid(form)

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
    permission_classes = (permissions.AllowAny,)

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (permissions.AllowAny,)

# Procedure Views
class ProcedureList(generics.ListCreateAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    permission_classes = (permissions.AllowAny,)

class ProcedureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    permission_classes = (permissions.AllowAny,)
    
# Equipment Views
class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (permissions.AllowAny,)

class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (permissions.AllowAny,)

# Comment Views
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

# Post Views
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

class PostListByRecipe(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

# Get posts by recipe
    def get_queryset(self):
        recipe = self.kwargs['recipe']
        return Post.objects.filter(recipe=recipe)
  

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()



# Chat room test
def index(request):
    return render(request, 'example/index.html')

def room(request, room_name):
    return render(request, 'example/room.html', {
        'room_name': room_name
    })