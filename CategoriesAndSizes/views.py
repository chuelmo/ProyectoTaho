from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required(login_url="/accounts/login/")
def file_list(request):
    return render(request, 'file_list.html')
