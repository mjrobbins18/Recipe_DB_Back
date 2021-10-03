from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Models

# User Model
class User(AbstractUser):
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)

# Recipe
class Recipe(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, to_field="username",on_delete=models.CASCADE, related_name='user_recipe', null=True)

    def __str__(self):
        return str(self.title)

# Recipe Model 
class RecipeBody(models.Model):
    title = models.ForeignKey(Recipe,on_delete=models.CASCADE, related_name='recipe_body', null=True)
    image = models.ImageField(upload_to='images', blank=True)
    image_url = models.URLField(max_length=500, default='https://drive.google.com/uc?export=view&id=1m1fHXCN-JA_4nNLdH5eeqStS-gAoFWNU', blank=True)
    dish_components = models.CharField(max_length=1000, blank=True, default='')
    recipe_yield = models.CharField(max_length=500, blank=True, null=True)
    BREAD = 'Bread'
    CANAPE = 'Canape'
    CHEESE = 'Cheese'
    CHIPS = 'Chips'
    CORE = 'Core'
    OIL = 'Oil'
    PASTA = 'Pasta'
    PRESERVATION = 'Preservation'
    STARCH = 'Starch'
    VEGETABLE = 'Vegetable'
    TECHNIQUE = 'Technique'
    FIRST_COURSE = 'First Course'
    MEAT = 'Meat'
    MISC = 'Miscellaneous'
    STOCK = 'Stock'

    CATEGORY_CHOICES = [
        (BREAD,'Bread'),
        (CANAPE,'Canape'), 
        (CHEESE,'Cheese'),
        (CHIPS,'Chips'),
        (CORE,'Core'),
        (OIL,'Oils'),
        (PASTA, 'Pasta'),
        (PRESERVATION, 'Preservation'), 
        (STARCH,'Starch'), 
        (VEGETABLE,'Vegetable'), 
        (TECHNIQUE,'Technique'),
        (FIRST_COURSE,'First Course'),
        (MEAT,'Meat'), 
        (MISC,'Miscellaneous'), 
        (STOCK,'Stock'), 
    ]
    category = models.CharField(
        max_length=100,
        blank=True,
        choices= CATEGORY_CHOICES,
        default=None
    )
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)

class Ingredient(models.Model):
    quantity = models.FloatField()
    unit_of_measure = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE, 
        related_name='ingredients')

    def __str__(self):
        return str(self.name)

class Equipment(models.Model):
    quantity = models.IntegerField()
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='equipment'
    )
    def __str__(self):
        return str(self.name)

class Procedure(models.Model):
    step = models.CharField(max_length=500)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='procedure'
    )
    def __str__(self):
        return str(self.step)
    
# Post and Comment Models
class Post(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE, related_name='user_post')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_post')
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)

class Comment(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE, related_name='user_comment')
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


# Favorite Recipes

class Favorites(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE, related_name='user_favorite')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorite_recipe')

    def __str__(self):
        return str(self.user)

# Simpler Recipe Model
