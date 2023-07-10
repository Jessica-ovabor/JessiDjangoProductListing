from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


# Create your login views here.

def login_view(request):
    if request.method == "POST":
       login_form = AuthenticationForm(request=request, data=request.POST)
       if login_form.is_valid():
           username = login_form.cleaned_data.get("username")
           password = login_form.cleaned_data.get("password")
           user = authenticate(username=username, password=password)
           if user is not None:
               pass
           else:
               pass
    elif request.method == "GET":
        login_form = AuthenticationForm()
    return render(request, 'login.html',{'login_form':login_form})