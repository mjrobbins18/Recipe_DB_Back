from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.filters import OrderingFilter
from .serializers import RecipeSerializer, MyTokenObtainPairSerializer, CustomUserSerializer
from .models import Recipe

# Recipe Views
class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class ObtainTokenPairWithNameView(TokenObtainPairView):
    # permission_classes = (permissions.AllowAny,)
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

class HelloWorldView(APIView):

    def get(self, request):
        return Response(data={"hello":"world"}, status=status.HTTP_200_OK)

# User Views

# class UserViewSet(viewsets.ModelViewSet):
#     http_method_names = ['get']
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated)
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['updated']
#     ordering = ['-updated']

#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return User.objects.all()

#     def get_objects(self):
#         lookup_field_value = self.kwargs[self.lookup_field]

#         obj = User.objects.get(lookup_field_value)
#         self.check_object_permissions(self.request, obj)

#         return obj

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
