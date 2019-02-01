from django.shortcuts import render
from .models import Category
from .forms import CategoryForm

# Create your views here.
def category_list(request):
    categories = Category.objects.order_by('name')
    return render(request, 'tracker/category_list.html',{'categories' : categories})

def category_new(request):
    form = CategoryForm()
    return render(request, 'tracker/category_edit.html', {'form': form})
