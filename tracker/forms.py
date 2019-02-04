from django import forms
from .models import Category
from .models import Catalog
from .models import Producer

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
        fields = ('name', 'color', 'tastingnotes')
