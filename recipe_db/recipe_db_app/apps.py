from django.apps import AppConfig


class RecipeDbAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe_db_app'
# class UserConfig(AppConfig):
#     name = 'recipe.user'
#     label = 'recipe_user'