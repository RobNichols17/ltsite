from django.db import models
from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('name', 'variety', 'description')

class ProducerForm(forms.ModelForm):
    
    class Meta:
        model = Producer
        fields = ('name', 'state', 'country')


class CatalogForm(forms.ModelForm):

    class Meta:
        model = Catalog
        fields = ('name', 'producerid', 'categoryid', 'description', 'color',
                  'tastingnotes', 'imgname')
        labels  = {
                'producerid': ('Producer'),
                'categoryid': ('Category'),
                'tastingnotes': ('Tasting Notes'),
        }

class CatalogDeleteForm(forms.ModelForm):

    class Meta:
        model = Catalog
        fields = ('name', 'producerid', 'description')
        labels  = {
                'producerid': ('Producer'),
                'categoryid': ('Category'),
        }

class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ('catalogid', 'quantity')
        labels  = {
                'catalogid': ('Item'),
        }

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'description')

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('recipeid', 'catalogid')
        labels  = {
                'recipeid': ('Recipe'),
                'catalogid': ('Item'),
        }

class IngredientRecipeFilterForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('recipeid',)
        labels  = {
                'recipeid': ('Recipe'),
        }

