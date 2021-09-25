from django.urls import path
from . import views
from .views import ObtainTokenPairWithNameView, CustomUserCreate, HelloWorldView, LogoutAndBlacklistRefreshTokenForUserView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('recipes/view', views.RecipeList.as_view(), name='recipe_list'),
    path('recipes/create', views.RecipeCreate.as_view(), name='recipe_list'),
    path('recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('user/<str:username>', views.UserDetail.as_view(), name='user_list'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithNameView.as_view(), name='token_create'),  # override sjwt stock token
    # path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name = 'blacklist'),
   
]