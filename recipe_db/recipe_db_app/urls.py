from django.urls import path
from django.conf.urls import url
from . import views
from .views import ObtainTokenPairWithNameView, CustomUserCreate, LogoutAndBlacklistRefreshTokenForUserView, index
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('recipes/view', views.RecipeList.as_view(), name='recipe_list'),
    path('recipes/create', views.RecipeTitleCreate.as_view(), name='recipe_list'),
    path('recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipes/search/', views.RecipeSearch.as_view(), name='recipe_search'),
    path('recipes/title/<str:title>', views.RecipeListByTitle.as_view(), name='recipe_title_list'),
    path('recipes/user/<str:user>', views.RecipeListByUser.as_view(), name='recipe_user_list'),
    path('recipes/body/create', views.RecipeBodyCreate.as_view(), name='recipe_body'),
    path('recipes/body/<int:pk>', views.RecipeBodyDetail.as_view(), name='recipe_body_detail'),
    path('procedure/create', views.ProcedureList.as_view(), name='procedure_list'),
    path('procedure/<int:pk>', views.ProcedureDetail.as_view(), name='procedure_detail'),
    path('equipment/create', views.EquipmentList.as_view(), name='equipment_list'),
    path('equipment/<int:pk>', views.EquipmentDetail.as_view(), name='equipment_detail'),
    path('ingredient/create', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredient/<int:pk>', views.IngredientDetail.as_view(), name='ingredient_detail'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/recipe/<int:recipe>', views.PostListByRecipe.as_view(), name='post_lists'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('comment/', views.CommentList.as_view(), name='comment_list'),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
    path('user/<str:username>', views.UserDetail.as_view(), name='user_list'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithNameView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
   
]