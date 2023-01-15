from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('products/', views.ProductViewSet.as_view({'get': 'list'})),
    path('products/<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve'})),
    path('categories/', views.CategoriesViewSet.as_view({'get': 'list'})),
    path('categories/<int:pk>', views.CategoriesViewSet.as_view({'get': 'retrieve'})),
    path('categories/<int:id>/products/', views.FilteredProductViewSet.as_view({'get': 'list'})),
]
