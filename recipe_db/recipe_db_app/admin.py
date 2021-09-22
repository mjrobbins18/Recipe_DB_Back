from django.contrib import admin
from .models import Recipe, Ingredient, Equipment, Procedure

# Register your models here.
class IngredientInline(admin.TabularInline):
    model = Ingredient

class EquipmentInline(admin.TabularInline):
    model = Equipment

class ProcedureInline(admin.TabularInline):
    model = Procedure

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, 
               EquipmentInline, 
               ProcedureInline,  ]