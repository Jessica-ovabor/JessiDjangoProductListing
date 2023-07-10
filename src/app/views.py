from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def main_view(request):
    return render(request,'main.html')
@login_required
def home_view(request):
    return render(request,'home.html')
    

