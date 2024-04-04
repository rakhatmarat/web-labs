from django.urls import path, re_path
from api import views


urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:product_id>', views.product_details),
    path('categories', views.categories_list),
    path('categories/<int:category_id>/', views.categories_details),
    path('categories/<int:category_id>/products', views.products_by_category)
]
