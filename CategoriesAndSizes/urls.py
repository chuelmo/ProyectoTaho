from django.urls import re_path, path
from . import views

# namespace
app_name = "CategoriesAndSizes"

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('categories/', views.listCategories),
    path('categories/add/', views.createCategory),
    path('categories/del/<id>', views.deleteCategory),
    path('categories/edit/<id>', views.editCategory),
    path('categories/update/', views.updateCategory)
]