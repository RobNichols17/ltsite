from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm

# Create your views here.
def category_list(request):
    categories = Category.objects.order_by('name')
    return render(request, 'tracker/category_list.html',{'categories' : categories})

def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
#            return redirect('category_detail', pk=category.pk)
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'tracker/category_edit.html', {'form': form})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'tracker/category_detail.html', {'category': category})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
#            return redirect('category_detail', pk=category.pk)
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'tracker/category_edit.html', {'form': form})
