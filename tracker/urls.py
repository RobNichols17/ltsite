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
    path('producer/list/', views.producer_list, name='producer_list'),
    path('producer/<int:pk>/', views.producer_detail, name='producer_detail'),
    path('producer/new/', views.producer_new, name='producer_new'),
    path('producer/<int:pk>/edit/', views.producer_edit, name='producer_edit'),
    path('catalog/list/', views.catalog_list, name='catalog_list'),
    path('catalog/<int:pk>/', views.catalog_detail, name='catalog_detail'),
    path('catalog/new/', views.catalog_new, name='catalog_new'),
    path('catalog/<int:pk>/edit/', views.catalog_edit, name='catalog_edit'),
    path('inventory/list/', views.inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('inventory/new/', views.inventory_new, name='inventory_new'),
    path('inventory/<int:pk>/edit/', views.inventory_edit, name='inventory_edit'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
