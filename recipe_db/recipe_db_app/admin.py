from django.contrib import admin
from .models import Recipe, Ingredient, Equipment, Procedure, User

# Register your models here.
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
    inlines = [IngredientInline, 
               EquipmentInline, 
               ProcedureInline,  ]