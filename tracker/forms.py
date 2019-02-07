from django import forms
from .models import Category
from .models import Catalog
from .models import Producer
from .models import Inventory

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
        fields = ('name', 'producerid', 'categoryid', 'description', 'color', 'tastingnotes')
        labels  = {
                'producerid': ('Producer'),
                'categoryid': ('Category'),
                'tastingnotes': ('Tasting Notes'),
        }

class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ('catalogid', 'quantity', 'acquiredate')
        labels  = {
                'catalogid': ('Item'),
                'acquiredate': ('Date Acquired'),
        }
