from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import SizeCategory, Size

def home(request):
    return render(request, "home.html")

@login_required(login_url="/accounts/login/")
def file_list(request):
    return render(request, 'file_list.html')

@login_required(login_url="/accounts/login/")
def listCategories(request):
    allCategories = SizeCategory.objects.all()
    return render(request, 'crudCategories.html', {'categories': allCategories})

@login_required(login_url="/accounts/login/")
def createCategory(request):
    nombre = request.POST['txtDescription']
    categoria = SizeCategory.objects.create(description=nombre)
    return redirect('/files/categories/')

@login_required(login_url="/accounts/login/")
def editCategory(request, id):
    categoria = SizeCategory.objects.get(id=id)
    return render(request, "editCategory.html", {"category": categoria})

@login_required(login_url="/accounts/login/")
def deleteCategory(request, id):
    categoria = SizeCategory.objects.get(id=id)
    categoria.delete()
    return redirect('/files/categories/')

@login_required(login_url="/accounts/login/")
def updateCategory(request):
    id = request.POST['txtId']
    nombre = request.POST['txtDescription']
    categoria = SizeCategory.objects.get(id=id)
    categoria.description = nombre
    categoria.save()
    return redirect('/files/categories/')