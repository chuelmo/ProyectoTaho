from django.urls import re_path, path
from . import views

# namespace
app_name = "CategoriesAndSizes"

urlpatterns = [
    path('', views.file_list, name='file_list'),
]