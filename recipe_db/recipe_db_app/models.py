from django.db import models

# Models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    image_url = models.URLField(blank= True)
    dish_components = models.CharField(max_length=500, blank=True)
    author = models.CharField(max_length=40)
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
        max_length=14,
        choices=CATEGORY_CHOICES,
        blank=True,
        default=None
    )

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    quantity = models.FloatField()
    unit_of_measure = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name='ingredients')

    def __str__(self):
        return self.name

class Equipment(models.Model):
    quantity = models.IntegerField()
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='equipment'
    )
    def __str__(self):
        return self.name

class Procedure(models.Model):
    step = models.CharField(max_length=500)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='procedure'
    )
    def __str__(self):
        return self.step