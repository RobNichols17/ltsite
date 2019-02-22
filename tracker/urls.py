from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category/list/', views.category_list, name='category_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/new/', views.category_new, name='category_new'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', views.category_delete,
         name='category_delete'),
    path('producer/list/', views.producer_list, name='producer_list'),
    path('producer/<int:pk>/', views.producer_detail, name='producer_detail'),
    path('producer/new/', views.producer_new, name='producer_new'),
    path('producer/<int:pk>/edit/', views.producer_edit, name='producer_edit'),
    path('producer/<int:pk>/delete/', views.producer_delete,
         name='producer_delete'),
    path('catalog/list/', views.catalog_list, name='catalog_list'),
    path('catalog/<int:pk>/', views.catalog_detail, name='catalog_detail'),
    path('catalog/new/', views.catalog_new, name='catalog_new'),
    path('catalog/<int:pk>/edit/', views.catalog_edit, name='catalog_edit'),
    path('catalog/<int:pk>/delete/', views.catalog_delete, name='catalog_delete'),
    path('inventory/list/', views.inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('inventory/new/', views.inventory_new, name='inventory_new'),
    path('inventory/<int:pk>/edit/', views.inventory_edit, name='inventory_edit'),
    path('inventory/<int:pk>/delete/', views.inventory_delete,
         name='inventory_delete'),
    path('recipe/list/', views.recipe_list, name='recipe_list'),
    path('recipe/new/', views.recipe_new, name='recipe_new'),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', views.recipe_delete,
         name='recipe_delete'),
    path('ingredient/list/', views.ingredient_list, name='ingredient_list'),
    path('ingredient/new', views.ingredient_new, name='ingredient_new'),
    path('ingredient/<int:pk>/edit/', views.ingredient_edit, name='ingredient_edit'),
    path('ingredient/<int:pk>/delete/', views.ingredient_delete,
         name='ingredient_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
