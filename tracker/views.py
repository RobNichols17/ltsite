from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm
from .models import Producer
from .forms import ProducerForm
from .models import Catalog
from .forms import CatalogForm
from .models import Inventory
from .forms import InventoryForm

# Create your views here.
def main(request):
    return render(request, 'tracker/main.html',{})

# Start category views
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

# Start producer views
def producer_list(request):
    producers = Producer.objects.order_by('name')
    return render(request, 'tracker/producer_list.html',{'producers' : producers})

def producer_new(request):
    if request.method == "POST":
        form = ProducerForm(request.POST)
        if form.is_valid():
            producer = form.save(commit=False)
            producer.save()
#            return redirect('producer_detail', pk=producer.pk)
            return redirect('producer_list')
    else:
        form = ProducerForm()
    return render(request, 'tracker/producer_edit.html', {'form': form})

def producer_detail(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    return render(request, 'tracker/producer_detail.html', {'producer': producer})

def producer_edit(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    if request.method == "POST":
        form = ProducerForm(request.POST, instance=producer)
        if form.is_valid():
            producer = form.save(commit=False)
            producer.save()
#            return redirect('producer_detail', pk=producer.pk)
            return redirect('producer_list')
    else:
        form = ProducerForm(instance=producer)
    return render(request, 'tracker/producer_edit.html', {'form': form})

# Start catalog views
def catalog_list(request):
    catalogs = Catalog.objects.order_by('name')
    return render(request, 'tracker/catalog_list.html',{'catalogs' : catalogs})

def catalog_new(request):
    if request.method == "POST":
        form = CatalogForm(request.POST)
        if form.is_valid():
            catalog = form.save(commit=False)
            catalog.save()
#            return redirect('catalog_detail', pk=catalog.pk)
            return redirect('catalog_list')
    else:
        form = CatalogForm()
    return render(request, 'tracker/catalog_edit.html', {'form': form})

def catalog_detail(request, pk):
    catalog = get_object_or_404(Catalog, pk=pk)
    return render(request, 'tracker/catalog_detail.html', {'catalog': catalog})

def catalog_edit(request, pk):
    catalog = get_object_or_404(Catalog, pk=pk)
    if request.method == "POST":
        form = CatalogForm(request.POST, instance=catalog)
        if form.is_valid():
            catalog = form.save(commit=False)
            catalog.save()
#            return redirect('catalog_detail', pk=catalog.pk)
            return redirect('catalog_list')
    else:
        form = CatalogForm(instance=catalog)
    return render(request, 'tracker/catalog_edit.html', {'form': form})

# Start inventory views
def inventory_list(request):
    inventories = Inventory.objects.order_by('catalogid')
    return render(request, 'tracker/inventory_list.html',{'inventories' : inventories})

def inventory_new(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.save()
#            return redirect('inventory_detail', pk=inventory.pk)
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'tracker/inventory_edit.html', {'form': form})

def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    return render(request, 'tracker/inventory_detail.html', {'inventory': inventory})

def inventory_edit(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.save()
#            return redirect('inventory_detail', pk=inventory.pk)
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'tracker/inventory_edit.html', {'form': form})
