from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

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

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = categoryForm(request.POST, instance=category)

        if form.is_valid(): # checks CSRF
            category.delete()
            return redirect("category_list") 

    else:
        form = categoryForm(instance=category)

    return render(request, 'tracker/category_delete.html', {'form': form})

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

def producer_delete(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = producerForm(request.POST, instance=producer)

        if form.is_valid(): # checks CSRF
            producer.delete()
            return redirect("producer_list") 

    else:
        form = producerForm(instance=producer)

    return render(request, 'tracker/producer_delete.html', {'form': form})

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

def catalog_delete(request, pk):
    catalog = get_object_or_404(Catalog, pk=pk)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = CatalogDeleteForm(request.POST, instance=catalog)

        if form.is_valid(): # checks CSRF
            catalog.delete()
            return redirect("catalog_list") 

    else:
        form = CatalogDeleteForm(instance=catalog)

    return render(request, 'tracker/catalog_delete.html', {'form': form})

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

def inventory_delete(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)

        if form.is_valid(): # checks CSRF
            inventory.delete()
            return redirect("inventory_list") 

    else:
        form = InventoryForm(instance=inventory)

    return render(request, 'tracker/inventory_delete.html', {'form': form})

# Start recipe views
def recipe_list(request):
    recipes = Recipe.objects.order_by('name')
    return render(request, 'tracker/recipe_list.html',{'recipes' : recipes})

def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
#            return redirect('recipe_detail', pk=recipe.pk)
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'tracker/recipe_edit.html', {'form': form})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
#            return redirect('recipe_detail', pk=recipe.pk)
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'tracker/recipe_edit.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)

        if form.is_valid(): # checks CSRF
            recipe.delete()
            return redirect("recipe_list") 

    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'tracker/recipe_delete.html', {'form': form})

# Start ingredient views
def ingredient_list(request):
    recipes = Recipe.objects.order_by('name')
    ingredients = Ingredient.objects.order_by('recipeid', 'catalogid')
    recform = IngredientRecipeFilterForm(request.GET)
    return render(request, 'tracker/ingredient_list.html',{'ingredients' :
                                                           ingredients,
                                                           'recipes': recipes,
                  'recform': recform})
def ingredient_list_filter(request):
    ingredients = Ingredient.objects.order_by('recipeid', 'catalogid')
    return render(request, 'tracker/ingredient_list.html',{'ingredients' :
                                                           ingredients})
def ingredient_new(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
#            return redirect('ingredient_detail', pk=ingredient.pk)
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'tracker/ingredient_edit.html', {'form': form})

def ingredient_edit(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
#            return redirect('ingredient_detail', pk=ingredient.pk)
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'tracker/ingredient_edit.html', {'form': form})

def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)

        if form.is_valid(): # checks CSRF
            ingredient.delete()
            return redirect("ingredient_list") 

    else:
        form = IngredientForm(instance=ingredient)

    return render(request, 'tracker/ingredient_delete.html', {'form': form})

