from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/new/', views.category_new, name='category_new'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('catalog/<int:pk>/', views.catalog_detail, name='catalog_detail'),
    path('catalog/new/', views.catalog_new, name='catalog_new'),
    path('catalog/<int:pk>/edit/', views.catalog_edit, name='catalog_edit'),
]
