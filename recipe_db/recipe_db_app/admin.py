from django.contrib import admin
from .models import Recipe, Ingredient, Equipment, Procedure, User, RecipeBody

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

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [BodyInline,
               IngredientInline, 
               EquipmentInline, 
               ProcedureInline,  ]