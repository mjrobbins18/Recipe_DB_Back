from django.urls import path
from . import views
from .views import ObtainTokenPairWithNameView, CustomUserCreate, LogoutAndBlacklistRefreshTokenForUserView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('recipes/view', views.RecipeList.as_view(), name='recipe_list'),
    path('recipes/create', views.RecipeTitleCreate.as_view(), name='recipe_list'),
    path('recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipes/search/', views.RecipeSearch.as_view(), name='recipe_search'),
    path('recipes/user/<str:user>', views.RecipeList.as_view(), name='recipe_user_list'),
    path('recipes/body/create', views.RecipeBodyCreate.as_view(), name='recipe_body'),
    path('procedure/create', views.ProcedureList.as_view(), name='recipe_list'),
    path('equipment/create', views.EquipmentList.as_view(), name='recipe_list'),
    path('ingredient/create', views.IngredientList.as_view(), name='recipe_list'),
    path('user/<str:username>', views.UserDetail.as_view(), name='user_list'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithNameView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name = 'blacklist'),
   
]