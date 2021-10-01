from django.contrib import admin
from .models import Post, Recipe, Ingredient, Equipment, Procedure, User, RecipeBody, Comment

# Register your models here.
class BodyInline(admin.TabularInline):
    model = RecipeBody

class IngredientInline(admin.TabularInline):
    model = Ingredient

class EquipmentInline(admin.TabularInline):
    model = Equipment

class ProcedureInline(admin.TabularInline):
    model = Procedure

class UserAdmin(admin.ModelAdmin):
    model = User

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [BodyInline,
               IngredientInline, 
               EquipmentInline, 
               ProcedureInline,  ]